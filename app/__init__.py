# pylint: disable=C0413
from flask import Flask
from app.config import Config as config_class
from app.exceptions import CustomException, handle_custom_exception
from app.extensions import db


app = Flask(__name__)
app.config.from_object(config_class)

# Register errors
app.register_error_handler(CustomException, handle_custom_exception)


# Register blueprints here
from app.auth.routes import bp as auth_bp

app.register_blueprint(auth_bp)

# Initialize extensions here
db.init_app(app)
