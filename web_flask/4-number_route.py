#!/usr/bin/python3i
"""start python app
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def is_fun(text):
    """c is fun route"""
    f_text = text = text.replace('_', ' ')
    return f'C {f_text}'


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """python route"""
    f_text = text.replace('_', ' ')
    return f"Python {f_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """number route"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
