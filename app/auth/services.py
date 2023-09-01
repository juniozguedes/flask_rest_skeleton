# pylint: disable=E1101
from app.auth.models import User, db
from app.auth.schemas import UserRequest


def create_user(data: UserRequest):
    user = User(email=data["email"], password=data["hashed_password"])
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user
