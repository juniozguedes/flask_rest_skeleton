# pylint: disable=W0611
from app.extensions import db
from app.subscriptions.models import Subscription


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    subscriptions = db.relationship("Subscription", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"
