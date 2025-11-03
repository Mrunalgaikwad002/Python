from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "404 Not Found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
