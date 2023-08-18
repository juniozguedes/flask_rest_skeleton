from app import ma


class UserResponse(ma.Schema):
    class Meta:
        fields = ("email", "token")


class UserRequest(ma.Schema):
    class Meta:
        fields = ("email", "password")


user_response_schema = UserResponse()
user_request_schema = UserRequest()
