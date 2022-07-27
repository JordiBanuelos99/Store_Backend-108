from flask import Flask, request
from about import me
from data import mock_data
import random
import json
from config import db
from bson import ObjectId

app = Flask('server')

@app.get("/")
def home():
    return "Hello from the Flask server"

@app.get("/test")
def test():
    return "This is just a simple text"

@app.get("/about")
def about():
    return "Jordi Bañuelos"

############## API ENDPOINTS = PRODUCTS ################

@app.get("/api/version")
def version():
    return "1.0"

@app.get("/api/about")
def about_json():
    return json.dumps(me)

def fix_mongo_id (obj):
    obj["id"] = str (obj["_id"])
    del obj["_id"]
    return obj

@app.get("/api/products")
def products_json():
    cursor= db.products.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    return json.dumps(results)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    product["_id"] = str(product["_id"])
    del product["_id"]

    return json.dumps(product)

@app.get("/api/products/<id>")
def get_product_by_id(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"
    
    fix_mongo_id(prod)
    return json.dumps(prod)

@app.get("/api/categories")
def category_list():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        cat = product["category"]
        if not product in categories:
            categories.append(cat)
    return json.dumps(categories)

# get return the number of prods in the catalog
# api/count_products
@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1
    return json.dumps({"count": count})

# get api/search/<text>
# return all prods whose title contains text
@app.get("/api/search/<text>")
def search_products(text):
    results= []
    # do the magic here
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod)
    return json.dumps(results)

# GET Category/products_category/<category>
# Return all products who's category is the one at the top
# create a results list
# travel the list, get every product
# if prod --> category is equal to the category variable
# add prod to the results list
# outside the for loop, return the results list as json
@app.get("/api/products_category/<category>")
def get_product_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for product in cursor:
        fix_mongo_id(product)
        results.append(product)
    return json.dumps(results)

# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest_product():
    cursor = db.products.find({})
    solution = cursor[0]
    for product in cursor:
        if product["price"] < solution["price"]:
            solution = product

    fix_mongo_id(solution)
    return json.dumps(solution)

app.run(debug=True)