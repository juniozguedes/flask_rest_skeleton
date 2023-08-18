from app.auth.models import User, db


def create_user(data):
    user = User(email=data["email"], password=data["hashed_password"])
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user
