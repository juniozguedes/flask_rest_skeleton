from datetime import datetime, timedelta
from marshmallow import ValidationError
from passlib.context import CryptContext
from flask import Blueprint, request
from jose import jwt
from app.auth.exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    WrongPasswordException,
)
from app.auth.schemas import user_response_schema, user_request_schema
from app import config_class
from app.auth.services import create_user, get_user_by_email
from app.exceptions import ValidationException


bp = Blueprint("auth", __name__, url_prefix="/auth")

user_db = []
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=config_class.ACCESS_TOKEN_EXPIRE_MINUTES)
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
        user_request_schema.validate(request.json)
        user_data = user_request_schema.load(request.json)
    except ValidationError as err:
        raise ValidationException(validation_message=err.messages) from err
    if get_user_by_email(user_data["email"]):
        raise UserAlreadyExistsException(email=user_data["email"])

    user_data["hashed_password"] = pwd_context.hash(user_data["password"])
    db_user = create_user(user_data)

    access_token = create_access_token({"sub": db_user.email})
    user_response = {"email": db_user.email, "token": access_token}
    return user_response_schema.dump(user_response)


@bp.route("/login", methods=["POST"])
def login():
    try:
        # Validate user_request
        user_data = user_request_schema.load(request.json)
    except ValidationError as err:
        raise ValidationException(validation_message=err.messages) from err
    db_user = get_user_by_email(user_data["email"])
    if not db_user:
        raise UserNotFoundException()
    if not pwd_context.verify(user_data["password"], db_user.password):
        raise WrongPasswordException()

    access_token = create_access_token({"sub": db_user.email})
    user_response = {"email": db_user.email, "token": access_token}
    return user_response_schema.dump(user_response)


@bp.route("/", methods=["GET"])
def hello_world():
    return {"Hello": "Hello"}
