from flask import Flask, render_template, request, url_for, jsonify

app = Flask('')

@app.route('/')
def _index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
