from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import requests
import json

app = Flask(__name__)


@app.route("/purchase/<item_number>",methods = ['GET'])
def purchaseCatServer(item_number):
    quantity=int(requests.get("http://catalog:5000/info/%s" % item_number).json()['quantity'])
    if quantity > 0 :
        obj = {"quantity": quantity - 1}
        requests.put("http://catalog:5000/update/%s" % item_number,json = obj)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}