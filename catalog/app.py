from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import csv
import json

app = Flask(__name__)




@app.route("/search/<category>")
def search(category):
    file = open('catalog.csv')
    csvreader = csv.reader(file, delimiter=',')
    s = ""
    flag = 0
    for line in csv.DictReader(file):
    	if line['Category'] == category:
    		flag = 1
    		line.pop('Category')
    		line.pop('quantity')
    		line.pop('price')
    		s+= json.dumps(line, indent = 4) + "<br>"
    file.close()
    if flag == 0: s+= "No matching category"
    return s
    
@app.route("/info/<item_number>")
def info(item_number):
    file = open('catalog.csv')
    csvreader = csv.reader(file, delimiter=',')
    s = ""
    flag = 0
    for line in csv.DictReader(file):
    	if line['ID'] == item_number:
    		flag = 1
    		line.pop('Category')
    		line.pop('ID')
    		s+= json.dumps(line, indent = 4) + "<br>"
    file.close()
    if flag == 0: s+= "No matching category"
    return s
