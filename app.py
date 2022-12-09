from flask import Flask
from flask_rest_skeleton.extensions import db, migrate
from flask_rest_skeleton.teams.models import User

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
      
def register_blueprints(app):
    from .teams.teams import teams_bp
    app.register_blueprint(teams_bp, url_prefix='/api/v1/teams')


def create_app():
    app = Flask("flask_rest_skeleton")
    app.config.from_object("flask_rest_skeleton.config.Config")
    configure_extensions(app)
    register_blueprints(app)
    return app

if __name__ == '__main__':
    app = create_app(False)
    app.run(host='0.0.0.0', port=5001)