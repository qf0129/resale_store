from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    _init_config(app)
    _init_db(app)
    _init_api(app)
    _init_login(app)
    return app

def _init_config(app):
    from app.config import BaseConfig
    app.config.from_object(BaseConfig)

def _init_db(app):
    db.init_app(app)


def _init_api(app):
    from app.api import init_api
    init_api(app)

def _init_login(app):
    login_manager.init_app(app)

    from flask import request, redirect
    from urllib.parse import quote
    
    def unauthorized():
        return redirect('/login?return=%s' % (quote(request.url)))
    login_manager.unauthorized = unauthorized

    from app.models import User
    @login_manager.user_loader
    def load_user(userid):
        return User.query.get(userid)

app = create_app()