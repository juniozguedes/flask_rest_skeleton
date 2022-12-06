from flask import Flask
from teams.teams import teams_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def myfunc():
    print('hey im func')
        

if __name__ == '__main__':
    print("starting app")
    myfunc()
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    app.register_blueprint(teams_bp, url_prefix='/api/v1/teams')

    with app.app_context():
        db.create_all()  # Create sql tables for our data models

        app.run()
    