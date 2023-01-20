#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def slash():
    """returns intro string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb content"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_flask(text):
    """return c is 'text' replacing underscores in text content"""
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_flask(text):
    """return python is 'text' replacing underscores in text content
        default = 'is cool'
    """
    text = text.replace('_', ' ')
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_flask(n):
    """returns only when argument is an integer"""
    return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_flask(n):
    """render html template with number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_flask(n):
    """render html template with a check if number is even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
