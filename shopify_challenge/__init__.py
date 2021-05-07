import os

from flask import Flask

from shopify_challenge.extensions import db
from shopify_challenge.routes.main import register_main_routes
from shopify_challenge.routes.util import register_util_routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATBASE_URL',
        'postgresql://postgres:postgres@localhost:5432/shopify-challenge'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    register_main_routes(app)
    register_util_routes(app)

    return app
