#!/usr/bin/python3
"""main app module"""
from flask import Flask, render_template, request
from flask_babel import Babel, localeselector


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


class Config:
    """
    Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """displays Welcome to Holberton"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Gets the best matching language for user """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
