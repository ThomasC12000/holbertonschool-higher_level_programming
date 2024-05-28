#!/usr/bin/python3
'''MODULE'''
import csv
import json

def convert_csv_to_json(csv_filename):
    '''
    Reading data from one format (CSV) and converting it into 
    another format (JSON) using serialization techniques
    '''
    try:
        data = []

        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                data.append(row)

        with open('data.json', mode='w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
