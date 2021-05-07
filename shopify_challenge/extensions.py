from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from shopify_challenge.views.home import Home
from shopify_challenge.views.user import User

home_view = Home.as_view('home_view')
user_view = User.as_view('user_view')