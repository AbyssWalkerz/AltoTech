from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .auth.routes import auth
    from .main.routes import main
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(auth)
    app.register_blueprint(main)
    
    return app