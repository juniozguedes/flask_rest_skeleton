from datetime import datetime, timedelta
from marshmallow import ValidationError
from passlib.context import CryptContext
from flask import Blueprint, jsonify, request
from jose import jwt
from app.auth.schemas import user_response_schema, user_request_schema
from app import config_class
from app.auth.services import create_user, get_user_by_email


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
        # Validate user_request
        user_data = user_request_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    if get_user_by_email(user_data["email"]):
        return {"User already exists"}

    user_data["hashed_password"] = pwd_context.hash("1234")
    db_user = create_user(user_data)

    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": db_user.email}, expires)
    user_response = {"email": db_user.email, "token": access_token}
    return user_response_schema.dump(user_response)


@bp.route("/login", methods=["POST"])
def login():
    try:
        user_data = user_request_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    user = get_user_by_email(user_data["email"])
    if not user:
        return "User does not exist"
    if not pwd_context.verify(user_data["password"], user.password):
        return "Wrong password"
    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": user.email}, expires)

    response = {"email": user.email, "token": access_token}
    return user_response_schema.dump(response)
