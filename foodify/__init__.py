import os

from flask import Flask
from flask_migrate import Migrate

from foodify.extensions import db
from foodify.routes.main import register_main_routes
from foodify.routes.util import register_util_routes


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:postgres@localhost:5432/shopify-challenge'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.secret_key = os.getenv("SECRET")
    
    db.init_app(app)
    Migrate(app, db)

    @app.before_first_request
    def create_tables():
        db.create_all()

    register_main_routes(app)
    register_util_routes(app)

    return app
