from flask import Flask, Response, request
import json

app = Flask(__name__)

products = [{
    "id": 1,
    "name": "pressure cooker"
}]

@app.route('/')
def index():
    return "Hello World!"

@app.route("/api/products", methods=["GET"])
def get():
    print("get method executed")

    string = json.dumps(products)

    # try:
    #     for product in products:
    #         if(str(product["id"]) == request.args["id"]):
    #             string = json.dumps(product)
    #             break
    # except Exception as e:
    #     string = json.dumps(products)

    response = Response()

    response.set_data(string)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route("/api/product/<id>", methods=["GET"])
def get_by_id(id):
    int_id = int(id)
    string = ""

    for product in products:
        if product["id"] == int_id:
            string = json.dumps(product)
            break

    response = Response()
    response.set_data(string)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route("/api/products", methods=["POST"])
def post():
    print("post method executed")

    # we got content from request
    content = request.get_data()

    # we parsed that content to dictionary
    product = json.loads(content)
    product["id"] = len(products) + 1

    # added new product dictionary to products list
    products.append(product)

    # stringified products list
    string = json.dumps(products)

    response = Response()

    response.set_data(string)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route("/api/product/<id>", methods=["PUT"])
def put(id):
    response = Response()
    int_id = int(id)
    incoming_product = json.loads(request.get_data())
    incoming_product["id"] = int_id

    for idx, product in enumerate(products):
        print(product)
        print(int_id)
        if(product["id"] == int_id):
            del products[idx]
            products.insert(idx, incoming_product)
            response.set_data(json.dumps(incoming_product))
            break

    return response

@app.route("/products")
def home():
    response = Response()

    response.set_data("<html><head></head><body>Hello</body></html>")
    response.headers["Content-Type"] = "text/html"
    
    return response

app.run()

# @app.route("/products", )
# def post():
#     pass

# @app.route("/products")
# def put():
#     pass

# @app.route("/products")
# def delete():
#     pass