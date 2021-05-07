from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from shopify_challenge.views.home import Home
from shopify_challenge.views.register import Register
from shopify_challenge.views.login import Login

home_view = Home.as_view('home_view')
register_view = Register.as_view('register_view')
login_view = Login.as_view('login_view')