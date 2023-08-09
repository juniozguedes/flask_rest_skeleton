# encoding: utf-8

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
