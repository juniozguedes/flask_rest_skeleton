from flask import Flask

from app.config import Config as config_class
from app.extensions import db, ma
from app.auth.routes import bp as auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints here
    app.register_blueprint(auth_bp)

    # Initialize extensions here
    db.init_app(app)
    ma.init_app(app)
    return app
