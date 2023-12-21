#!/usr/bin/python3i
"""start python app
"""
from flask import Flask
app= Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def is_fun(text):
    f_text = text = text.replace('_', ' ')
    return f'C {f_text}'

@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text= 'is cool'):
    f_text = text.replace('_', ' ')
    return f"Python {f_text}"

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')  

