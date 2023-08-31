from typing import Optional
from pydantic import BaseModel


class UserRequest(BaseModel):
    email: str
    password: str
    hashed_password: Optional[str] = None


class UserResponse(BaseModel):
    email: str
    token: str
