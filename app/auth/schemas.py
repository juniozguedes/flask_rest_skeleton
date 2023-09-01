from marshmallow import Schema, fields


class UserRequest(Schema):
    email: fields.Str(required=True)
    password: fields.Str(required=True)

    # Fields to show when sending data:
    class Meta:
        fields = ["email", "password"]


class UserResponse(Schema):
    email: fields.Str(required=True)
    token: fields.Str(required=True)

    class Meta:
        fields = ("email", "token")


user_response_schema = UserResponse()
user_request_schema = UserRequest()
