from flask import render_template
from flask import Blueprint
from app.auth.models import User

bp = Blueprint("auth", __name__)

response = [
    {"email": "user@email.com", "password": "1234"},
    {"email": "user@email.com", "password": "1234"},
]


@bp.route("/auth/")
def auth():
    users = User.query.all()
    return render_template("posts/categories.html")
