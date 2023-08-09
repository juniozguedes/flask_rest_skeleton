from flask import Flask

from config import Config as config_class
from app.extensions import db, ma
from app.auth.routes import bp as auth_bp


app = Flask(__name__)
app.config.from_object(config_class)

# Initialize extensions here
db.init_app(app)
ma.init_app(app)

# Register blueprints here
app.register_blueprint(auth_bp, url_prefix="/auth")
