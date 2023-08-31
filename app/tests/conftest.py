# pylint: disable=E1101

import os
import tempfile
import pytest
from app import app
from app.config import Config


class TestSettings(Config):
    TESTING = True


@pytest.fixture
def client():
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        with app.app_context():
            app.init_db()
        yield test_client

    os.close(db_fd)
    os.unlink(app.app.config["DATABASE"])
