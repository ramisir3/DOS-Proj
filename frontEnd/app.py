from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import requests

app = Flask(__name__)




@app.route("/search/<category>",methods = ['GET'])
def searchCatServer(category):
    return requests.get("http://catalog:5000/search/%s" % category).content
    
@app.route("/info/<item_number>",methods = ['GET'])
def infoCatServer(item_number):
    return requests.get("http://catalog:5000/info/%s" % item_number).content

@app.route("/purchase/<item_number>",methods = ['GET'])
def purchaseCatServer(item_number):
    return requests.get("http://order:5000/purchase/%s" % item_number).content