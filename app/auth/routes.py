from flask import Blueprint
from app.auth.schemas import user_schema

# from app.auth.models import User

bp = Blueprint("auth", __name__)

response = [
    {"email": "user@email.com", "token": "1234"},
    {"email": "user@email.com", "token": "1234"},
]


@bp.route("/", methods=["POST"])
def auth():
    user = response[0]
    return user_schema.dump(user)
