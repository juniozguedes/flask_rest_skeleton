# pylint: disable=W0611
from app.auth.models import User
from app.products.models import Product
from app.subscriptions.models import Subscription


def create(app, db_session):
    with app.app_context():
        db_session.create_all()
