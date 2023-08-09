from app.extensions import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "flasksqlalchemy-tutorial-users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)

    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
