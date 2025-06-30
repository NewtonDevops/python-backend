from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Hello from the Python backend!"), 200

if __name__ == "__main__":
    # Listen on all interfaces so Kubernetes can reach the container
    app.run(host="0.0.0.0", port=8080)
