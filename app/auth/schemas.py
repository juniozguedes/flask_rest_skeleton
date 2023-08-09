from app import ma


class UserResponse(ma.Schema):
    class Meta:
        fields = ("email", "token")


user_schema = UserResponse()
# users_schema = UserSchema(many=True)
