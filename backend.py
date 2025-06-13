from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Use /status/<code> to test error responses."

@app.route('/status/<int:code>')
def return_status(code):
    if code in [500, 501, 503, 504]:
        return jsonify({"error": f"Returning status code {code}"}), code
    return jsonify({"message": "Only 500, 501, 503, 504 supported"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
