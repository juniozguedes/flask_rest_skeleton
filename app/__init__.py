from flask import Flask

from config import Config
from app.extensions import db
from app.auth.routes import bp as auth_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app


create_app()
