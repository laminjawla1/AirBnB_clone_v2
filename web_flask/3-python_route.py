#!/usr/bin/python3
"""
This flask script sends a response with the message "Hello HBNB!"
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloHBNB():
    """Send a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
