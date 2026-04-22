from flask import Flask, jsonify, request
from data import products
from cart import add_to_cart, get_cart, clear_cart

app = Flask(__name__)

# 📦 получить товары
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

# 🛒 добавить в корзину
@app.route("/cart/add", methods=["POST"])
def add():
    data = request.json
    product_id = data["id"]
    cart = add_to_cart(product_id)
    return jsonify(cart)

# 🧺 посмотреть корзину
@app.route("/cart", methods=["GET"])
def cart_view():
    return jsonify(get_cart())

# 🧹 очистить корзину
@app.route("/cart/clear", methods=["POST"])
def clear():
    return jsonify(clear_cart())

if __name__ == "__main__":
    app.run(debug=True)

    from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from data import products

@app.route("/cart", methods=["GET"])
def cart_view():
    result = []
    for id in get_cart():
        for p in products:
            if p["id"] == id:
                result.append(p)
    return jsonify(result)