from flask import Blueprint
from app.auth.schemas import user_schema
from app import config_class


bp = Blueprint("auth", __name__, url_prefix="/auth")  # from app.auth.models import User

response = [
    {"email": "user@email.com", "token": "1234"},
    {"email": "user@email.com", "token": "1234"},
]


@bp.route("/", methods=["POST"])
def auth():
    print(config_class.SQLALCHEMY_DATABASE_URI)
    user = response[0]
    return user_schema.dump(user)
