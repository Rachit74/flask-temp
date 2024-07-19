from flask import Flask
from .views import *
from .auth import *

from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "QWE123"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')

    from . import models

    create_database(app)

    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created")