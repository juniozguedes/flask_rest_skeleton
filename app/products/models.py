from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    short_code = db.Column(db.String(20), index=True, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    subscriptions = db.relationship("Subscription", backref="product", lazy=True)

    def __repr__(self):
        return f"<Product {self.short_code}>"
