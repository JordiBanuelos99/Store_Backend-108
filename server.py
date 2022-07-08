from flask import Flask
from about import me
from data import mock_data
import json

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

@app.get("/api/products")
def products_json():
    return json.dumps(mock_data)

@app.get("/api/products/<id>")
def get_product_by_id(id):
    for product in mock_data:
        if str(product["id"]) == id:
            return json.dumps(product)
    return "NOT FOUND"

@app.get("/api/categories")
def category_list():
    categories = []
    for item in mock_data:
        if not item["category"] in categories:
            categories.append(item["category"])
    return json.dumps(categories)

# GET Category/products_category/<category>
# Return all products who's category is the one at the top
# create a results list
# travel the list, get every product
# if prod --> category is equal to the category variable
# add prod to the results list
# outside the for loop, return the results list as json
@app.get("/api/products_category/<category>")
def get_product_by_category(category):
    categories = []
    for product in mock_data:
        if product["category"].lower() == category.lower():
            categories.append(product)
    return json.dumps(categories)

# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest_product():
    solution = mock_data[0]
    for product in mock_data:
        if product["price"] < solution["price"]:
            solution = product
    return json.dumps(solution)

app.run(debug=True)