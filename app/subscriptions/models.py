from app.extensions import db


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), index=True, nullable=False
    )
    product_id = db.Column(
        db.Integer, db.ForeignKey("products.id"), index=True, nullable=False
    )
    tier = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    # user cannot have multiple subscriptions to the same product
    db.UniqueConstraint(
        "user_id", "product_id", name="unique_user_product_subscription"
    )

    def __repr__(self):
        return f"<Subscription {self.id}>"
