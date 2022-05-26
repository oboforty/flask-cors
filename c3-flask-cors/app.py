from flask import Flask, render_template, request, url_for, jsonify
from flask_cors import CORS

app = Flask('')
CORS(app)

@app.route('/')
def _index():
    return "hello"

@app.route('/api/test')
def _api():

    return jsonify({
        "data": [
            {"id": 1, "val": 1},
            {"id": 2, "val": 5}
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10050, debug=True)
