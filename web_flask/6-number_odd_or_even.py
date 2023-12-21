#!/usr/bin/python3
"""start python app
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


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
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    result = f"{'odd' if int(n) % 2 != 0 else 'even'}"
    return render_template('6-number_odd_or_even.html', n=n, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')  
