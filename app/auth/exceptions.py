from app.exceptions import CustomException


class UserAlreadyExistsException(CustomException):
    def __init__(self, email):
        message = f"User '{email}' already exists"
        super().__init__(message, code=409)  # 409 Conflict status code


class UserNotFoundException(CustomException):
    def __init__(self):
        message = "User not found"
        super().__init__(message, code=404)  # 409 Conflict status code


class WrongPasswordException(CustomException):
    def __init__(self):
        message = "Wrong password"
        super().__init__(message, code=401)  # 409 Conflict status code
