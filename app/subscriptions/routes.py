from flask import Blueprint


bp = Blueprint("subscription", __name__, url_prefix="subscription")


@bp.route("/login", methods=["POST"])
def create_subscription():
    return True
