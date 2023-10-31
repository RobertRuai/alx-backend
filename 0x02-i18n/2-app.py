#!/usr/bin/python3
"""main app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    app.config.from_object(Config)


    @babel.localeselector
    def get_locale():
	    """get_locale func"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """displays Welcome to Holberton"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
