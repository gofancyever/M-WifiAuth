from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    #附加界面
    from .btdjy_app import btdjy as btdjy_blueprint
    app.register_blueprint(btdjy_blueprint)

    return app