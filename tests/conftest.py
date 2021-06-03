import os

import pytest

from foodify import create_app
from foodify.extensions import db


@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/shopify-challenge-test'

    client = app.test_client()
    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()