from flask import Flask
import requests
import json
import os

app = Flask(__name__)

#query to try and purchase a book by its ID if it is available in stock
@app.route("/purchase/<item_number>", methods=['GET'])
def purchaseCatServer(item_number):
	# check quantity in stock
    msg =requests.get(os.environ['CATALOG']+"/info/%s" % item_number)
    if msg.content.decode() == "Item not found :(":
        return msg.content
    quantity = int(msg.json()['quantity'])
    if quantity > 0:
		#if available in stock, update the quantity from the catalog server
        bookName = requests.put(os.environ['CATALOG']+"/update/%s" % item_number).content
        s = "Purchase complete :) bought book " + bookName.decode('UTF-8')
        return json.dumps(s), 200, {'ContentType': 'application/json'}
    else:
		#if not in stock, return failure message
        return json.dumps("Item not available in stock. Purchase failed :("), 400, {'ContentType': 'application/json'}
