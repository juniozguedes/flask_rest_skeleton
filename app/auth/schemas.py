from marshmallow import Schema, fields, validate


class UserRequest(Schema):
    email = fields.String(required=True, validate=validate.Email(), data_key="email")
    password: fields.String(required=True)

    class Meta:
        fields = ("email", "password")


class UserResponse(Schema):
    email: fields.Str(required=True)
    token: fields.Str(required=True)

    class Meta:
        fields = ("email", "token")


user_response_schema = UserResponse()
user_request_schema = UserRequest()
