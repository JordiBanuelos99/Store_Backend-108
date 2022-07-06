from flask import Flask

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
def about(me):
    return me["first"] + " " + me["last"]


app.run(debug=True)