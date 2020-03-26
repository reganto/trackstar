from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    config[config_name].init_app(app)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix="/users")

    return app

