from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import DevelopmentConfig

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app