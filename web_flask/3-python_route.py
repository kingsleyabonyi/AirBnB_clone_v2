#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
