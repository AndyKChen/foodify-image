from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from shopify_challenge.views.home import Home

home_view = Home.as_view('home_view')