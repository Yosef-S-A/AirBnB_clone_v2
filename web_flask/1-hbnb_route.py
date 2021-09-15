#!/usr/bin/python3


"""
a script that starts a Flask web application
with two route
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays "HBNB" '''
    return 'HBNB'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
