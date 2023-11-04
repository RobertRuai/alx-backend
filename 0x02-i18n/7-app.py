#!/usr/bin/python3
"""main app module"""
import flask
import pytz
from pytz.exceptions import UnkownTimeZoneError
from flask import Flask, g, render_template, request
from flask_babel import Babel


app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """displays Welcome to Holberton"""
    return render_template(
        '7-index.html', user=flask.g.user)


@babel.localeselector
def get_locale():
    """ Gets the best matching language for user """
    lan = request.args.get('locale')
    if lan is not None:
        if lan in app.config['LANGUAGES']:
            return lan
        elif g.users['locale'] in app.config['LANGUAGES']:
            return g.users['locale']
        else:
            return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(user_id):
    """ returns a user dictionary"""
     try:
        login_as = request.args.get('login_as')
        user_id = int(login_as)
        user = users.get(user_id)
        return user
    except Exception:
        return None


@app.before_request
def before_request():
    """use get_user to find a user"""
    user_id = request.args.get('login_as')
    flask.g.user = get_user(user_id)


@babel.timezoneselector
def get_timezone():
    """get a user timezone"""
    user = getattr(g, 'users', None)
    time = request.args.get("timezone")
    try:
        if pytz.timezone(time) is not None:
            if g.user['timezone'] is not None:
                return g.user['timezone']
            else:
                return request.accept_languages.best_match(
                    Config.BABEL_DEFAULT_TIMEZONE)
        return time
    except UnknownTimeZoneError:
        pass


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
