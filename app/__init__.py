from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    _init_config(app)
    _init_db(app)
    _init_api(app)
    return app

def _init_config(app):
    from app.config import BaseConfig
    app.config.from_object(BaseConfig)

def _init_db(app):
    db.init_app(app)

def _init_api(app):
    from app.api import init_api
    init_api(app)

app = create_app()