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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
