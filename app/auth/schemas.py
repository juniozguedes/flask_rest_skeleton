from app import ma


class UserResponse(ma.Schema):
    class Meta:
        fields = ("email", "token")


class UserRequest(ma.Schema):
    class Meta:
        fields = ("email", "password")


user_response = UserResponse()
user_request = UserRequest()
