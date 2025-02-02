#!/usr/bin/python3
"""
This flask script sends a response with the message "Hello HBNB!"
"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    n = int(n)
    result = "{} is ".format(n)
    if n % 2:
        result += "odd"
    else:
        result += "even"
    return render_template("6-number_odd_or_even.html", text=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
