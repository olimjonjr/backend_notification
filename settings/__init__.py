import os
from flask import Flask
from notify.database import db
from notify.views import views
from consumer import start
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database



def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    engine = create_engine(os.environ.get("SQLALCHEMY_DB_URI"))
    if not database_exists(engine.url):
        create_database(engine.url)

    if config is None:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=engine.url,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        ),
    else:
        app.config.from_mapping(config)

    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(views)

    start()

    return app
