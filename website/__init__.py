from flask import Flask
from .views import *
from .auth import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "QWE123"

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')

    return app