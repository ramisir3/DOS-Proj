from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import requests

app = Flask(__name__)




@app.route("/search/<category>")
def searchCatServer(category):
    return requests.get("http://catalog:5000/search/%s" % category).content
    
@app.route("/info/<item_number>")
def infoCatServer(item_number):
    return requests.get("http://catalog:5000/info/%s" % item_number).content