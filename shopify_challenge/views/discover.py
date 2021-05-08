import os

import boto3
from flask import redirect, render_template, session
from flask.views import MethodView


class Discover(MethodView):
    def get(self):
        ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
        SECRET_ACCESS_KEY = os.environ.get('SECRET_ACCESS_KEY')
        S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
        return render_template('discover.html')