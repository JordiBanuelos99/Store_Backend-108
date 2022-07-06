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
    return "Not found"


app.run(debug=True)