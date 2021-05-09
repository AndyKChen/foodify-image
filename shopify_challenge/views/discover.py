import os

import boto3
from flask import redirect, render_template, session
from flask.views import MethodView

from shopify_challenge.models.image import ImageModel
from shopify_challenge.helpers.config import CLOUDFRONT

class Discover(MethodView):
    def get(self):
        images = ImageModel.get_all_public_images()
        return render_template('discover.html', images=images, cloudfront=CLOUDFRONT)