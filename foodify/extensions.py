from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from foodify.views.discover import Discover
from foodify.views.login import Login
from foodify.views.personal import Personal
from foodify.views.register import Register
from foodify.views.upload import Upload

discover_view = Discover.as_view('discover_view')
register_view = Register.as_view('register_view')
login_view = Login.as_view('login_view')
upload_view = Upload.as_view('upload_view')
personal_view = Personal.as_view('personal_view')