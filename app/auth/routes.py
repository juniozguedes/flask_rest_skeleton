from datetime import datetime, timedelta
from marshmallow import ValidationError
from passlib.context import CryptContext
from flask import Blueprint, jsonify, request
from jose import jwt
from app.auth.models import User, db
from app.auth.schemas import user_response, user_request
from app import config_class


bp = Blueprint("auth", __name__, url_prefix="/auth")

user_db = []
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config_class.SECRET_KEY, algorithm=config_class.ALGORITHM
    )
    return encoded_jwt


@bp.route("/register", methods=["POST"])
def register_user():
    try:
        data = user_request.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # user = user_db[0]
    # if user:
    #    return user
    hashed_password = pwd_context.hash("1234")
    user = User(email=data["email"], password=hashed_password)
    db.session.add(user)
    db.session.commit()

    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": data["email"]}, expires)
    response = {"email": user.email, "token": access_token}
    return user_response.dump(response)


@bp.route("/login", methods=["POST"])
def login():
    request_password = "1234"
    request_email = "iamnew@gmail.com"

    user = user_db[0]
    if not pwd_context.verify(request_password, user["password"]):
        return "Wrong password"
    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": request_email}, expires)

    response = {"email": request_email, "token": access_token}
    return user_response.dump(response)
