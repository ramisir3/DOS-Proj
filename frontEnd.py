from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import csv
import json

app = Flask(__name__)




@app.route("/search/<category>")
def searchCatServer(category):
    return request.get(192.168.0.107:5000/search/category)
