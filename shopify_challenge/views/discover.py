import os

import boto3
from flask import redirect, render_template, session
from flask.views import MethodView

from shopify_challenge.models.image import ImageModel


class Discover(MethodView):
    def get(self):
        images = ImageModel.get_all_public_images()
        cloudfront = os.environ.get('CLOUDFRONT_DOMAIN')
        return render_template('discover.html', images=images, cloudfront=cloudfront)