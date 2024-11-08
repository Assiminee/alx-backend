#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Babel configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """ Renders 0-index.html file """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
