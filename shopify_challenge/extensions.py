from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from shopify_challenge.views.discover import Discover
from shopify_challenge.views.register import Register
from shopify_challenge.views.login import Login
from shopify_challenge.views.upload import Upload

discover_view = Discover.as_view('discover_view')
register_view = Register.as_view('register_view')
login_view = Login.as_view('login_view')
upload_view = Upload.as_view('upload_view')