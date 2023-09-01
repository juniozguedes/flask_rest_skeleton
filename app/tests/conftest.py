# pylint: disable=E1101,W0621
from faker import Faker
import pytest
from app import app
from app.config import Config

fake = Faker()


class TestSettings(Config):
    TESTING = True


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


RANDOM_STR = fake.email()
