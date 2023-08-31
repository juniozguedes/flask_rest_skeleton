from datetime import datetime, timedelta
from passlib.context import CryptContext
from flask import Blueprint
from jose import jwt
from flask_pydantic import validate as validate_request
from app.auth.exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    WrongPasswordException,
)
from app.auth.schemas import UserRequest, user_response_schema
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
@validate_request()
def register_user(body: UserRequest):
    if get_user_by_email(body.email):
        raise UserAlreadyExistsException(email=body.email)

    body.hashed_password = pwd_context.hash(body.password)
    db_user = create_user(body)

    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": db_user.email}, expires)
    user_response = {"email": db_user.email, "token": access_token}
    return user_response_schema.dump(user_response)


@bp.route("/login", methods=["POST"])
@validate_request()
def login(body: UserRequest):
    db_user = get_user_by_email(body.email)
    if not db_user:
        raise UserNotFoundException()
    if not pwd_context.verify(body.password, db_user.password):
        raise WrongPasswordException()
    expires = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": db_user.email}, expires)

    user_response = {"email": db_user.email, "token": access_token}
    return user_response_schema.dump(user_response)


@bp.route("/", methods=["GET"])
def hello_world():
    return "Hello"
