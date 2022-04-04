from flask import Flask
import csv
import json
import pandas as pd

app = Flask(__name__)

#search query to return all books
@app.route("/search", methods=['GET'])
def searchAll():
    file = open('catalog.csv')
    s = ""
    for line in csv.DictReader(file):
        line.pop('quantity')
        line.pop('price')
        s += json.dumps(line, indent=4)
    file.close()
    return s
	
	
#search query to return books in specific category
@app.route("/search/<category>", methods=['GET'])
def search(category):
    file = open('catalog.csv')
    s = ""
    flag = 0
    for line in csv.DictReader(file):
        if line['Category'] == category:
            flag = 1
            line.pop('Category')
            line.pop('quantity')
            line.pop('price')
            s += json.dumps(line, indent=4)
    file.close()
    if flag == 0:
        s += "No matching category"
    return s

# info query to return info about a specific book using its ID
@app.route("/info/<item_number>", methods=['GET'])
def info(item_number):
    file = open('catalog.csv')
    s = ""
    flag = 0
    for line in csv.DictReader(file):
        if line['ID'] == item_number:
            flag = 1
            line.pop('Category')
            line.pop('ID')
            s += json.dumps(line, indent=4)
    file.close()
    if flag == 0:
        s += "Item not found :("
    return s

#update query to decrement the quantity in stock after purchase
@app.route("/update/<item_number>", methods=['PUT'])
def update(item_number):
    df = pd.read_csv('catalog.csv')
    quantity =df.loc[int(item_number) - 1, 'quantity'] - 1
    df.loc[int(item_number)- 1, 'quantity'] = quantity
    df.to_csv('catalog.csv', index=False)
    return json.dumps({'successes': True}), 200, {'ContentType': 'application/json'}
