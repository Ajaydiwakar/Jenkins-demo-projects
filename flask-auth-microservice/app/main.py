import os
from flask import Flask, jsonify

app = Flask(__name__)

# Simulating secret retrieval from env vars
SECRET_KEY = os.environ.get('AUTH_SECRET', 'default-secret-if-not-set')

@app.route("/auth")
def auth():
    return jsonify({
        "status": "Auth Active", 
        "secret_length": len(SECRET_KEY),
        "message": "Secret successfully injected via CI/CD!" if SECRET_KEY != 'default-secret-if-not-set' else "Using default secret."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
