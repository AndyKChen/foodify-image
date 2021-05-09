import os
import pytest

from shopify_challenge import create_app
from shopify_challenge.extensions import db

@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/shopify-challenge-test'

    client = app.test_client()
    with app.app_context():
        app.secret_key = "secret"
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()