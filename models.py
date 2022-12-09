"""Data models."""
from flask_rest_skeleton.extensions import db


class Product(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'flasksqlalchemy-tutorial-users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80),index=True,unique=True,
        nullable=False)

    created = db.Column(db.DateTime,index=False,unique=False,
        nullable=False)

    admin = db.Column(db.Boolean,index=False,unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)