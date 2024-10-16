import json
from flask import Flask, jsonify, request, send_file, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return send_file('web/index.html')


@app.route('/clicked')
def text():
    return "<h1>Hello the button is clicked.</h1>"


if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))
