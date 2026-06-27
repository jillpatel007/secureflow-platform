from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="secureflow-api",
        message="Hello from the SecureFlow API",
        version="0.1.0",
    )

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    # 0.0.0.0 makes the server reachable from outside the container later
    app.run(host="0.0.0.0", port=8000)
