# pylint: disable=E1101
import orjson


class CustomException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ValidationException(CustomException):
    pass


class AuthenticationException(CustomException):
    pass


def handle_custom_exception(error):
    response_data = {"error": error.message}
    response = orjson.dumps(response_data)
    return response, error.code, {"Content-Type": "application/json"}
