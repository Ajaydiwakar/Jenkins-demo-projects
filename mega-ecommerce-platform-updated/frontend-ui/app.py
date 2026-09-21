import os, requests
from flask import Flask, jsonify

app = Flask(__name__)
PRODUCT_URL = os.environ.get('PRODUCT_URL', 'http://product-service:8081')
ORDER_URL = os.environ.get('ORDER_URL', 'http://order-service:8082')

@app.route("/")
def dashboard():
    try:
        prods = requests.get(f"{PRODUCT_URL}/api/products", timeout=2).json()
        orders = requests.get(f"{ORDER_URL}/api/orders", timeout=2).json()
        return jsonify({"dashboard": "Mega E-Commerce", "products": prods, "orders": orders})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)