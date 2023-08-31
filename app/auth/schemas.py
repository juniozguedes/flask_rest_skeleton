from typing import Optional
from pydantic import BaseModel
from app import ma


class UserRequest(BaseModel):
    email: str
    password: str
    hashed_password: Optional[str] = None


class UserResponse(ma.Schema):
    class Meta:
        fields = ("email", "token")


user_response_schema = UserResponse()
