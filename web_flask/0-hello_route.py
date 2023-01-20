#!/usr/bin/python3
"""starts a web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """returns into string"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
