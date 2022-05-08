from flask import Flask
import requests

app = Flask(__name__)
cache = {}
catalog1 = "http://catalog:5000"
oreder1 = "http://order:5000"

catalog2 = "http://catalog2:5000"
oreder2 = "http://order2:5000"


robin = False

#forward to catalog server
@app.route("/search", methods=['GET'])
def searchAllCatServer():
    global robin
    robin = not robin
    return requests.get(catalog1 if robin else catalog2+"/search").content

#forward to catalog server
@app.route("/search/<category>", methods=['GET'])
def searchCatServer(category):
    global robin
    robin = not robin
    if (category not in cache):
        cache[category] = requests.get(catalog1 if robin else catalog2+"/search/%s" % category).content
    return cache[category]

#forward to catalog server
@app.route("/info/<item_number>", methods=['GET'])
def infoCatServer(item_number):
    global robin
    robin = not robin
    if(item_number not in cache):
        cache[item_number] = requests.get(catalog1 if robin else catalog2+"/info/%s" % item_number).content
    print(cache)
    return cache[item_number]

#forward to order server
@app.route("/purchase/<item_number>", methods=['GET'])
def purchaseCatServer(item_number):
    global robin
    robin = not robin
    if (item_number in cache):
        cache.pop[item_number]
    return requests.get(oreder1 if robin else oreder2+"/purchase/%s" % item_number).content
