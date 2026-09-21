import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Backend URL injected via environment variable, defaulting to localhost for local dev
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8080')

@app.route("/")
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/api/data", timeout=5)
        backend_data = response.json()
        return jsonify({
            "frontend_status": "Active",
            "backend_response": backend_data
        })
    except Exception as e:
        return jsonify({
            "frontend_status": "Active",
            "backend_response": f"Failed to connect to backend at {BACKEND_URL}: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
