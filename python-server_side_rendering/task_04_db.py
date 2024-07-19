from flask import Flask, render_template, request, jsonify
import sqlite3
import csv
import json

app = Flask(__name__)

# Fonction pour lire les données de la base de données SQLite
def fetch_data_from_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, category FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'price': row[2],
            'category': row[3]
        }
        products.append(product)
    return products

# Fonction pour lire les données JSON
def fetch_data_from_json():
    with open('products.json') as json_file:
        data = json.load(json_file)
    return data

# Fonction pour lire les données CSV
def fetch_data_from_csv():
    products = []
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = {
                'id': row['id'],
                'name': row['name'],
                'price': float(row['price']),
                'category': row['category']
            }
            products.append(product)
    return products

@app.route('/')
def home():
    source = request.args.get('source', default='json', type=str)
    try:
        if source == 'json':
            products = fetch_data_from_json()
        elif source == 'csv':
            products = fetch_data_from_csv()
        elif source == 'sql':
            products = fetch_data_from_sqlite()
        else:
            return render_template('error.html', message='Wrong source'), 400
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)