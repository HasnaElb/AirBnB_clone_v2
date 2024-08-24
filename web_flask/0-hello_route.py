#!/usr/bin/python3
"""Simple Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello_hbnb():
    """Returns a string at the /airbnb-onepage/ route"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
