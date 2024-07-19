from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def fetch_json_data():
    with open('products.json') as f:
        return json.load(f)

def fetch_csv_data():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def fetch_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = fetch_json_data()
    elif source == 'csv':
        products = fetch_csv_data()
    elif source == 'sql':
        products = fetch_sql_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if str(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)