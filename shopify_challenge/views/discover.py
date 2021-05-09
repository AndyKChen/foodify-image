import os

import boto3
from flask import redirect, render_template, session, request, Response
from flask.views import MethodView
from io import BytesIO
import requests
import uuid

from shopify_challenge.models.image import ImageModel
from shopify_challenge.helpers.config import CLOUDFRONT
from shopify_challenge.helpers.s3_helpers import create_presigned_url

class Discover(MethodView):
    def get(self):
        images = ImageModel.get_all_public_images()
        return render_template('discover.html', images=images, cloudfront=CLOUDFRONT)

    def post(self):
        identifier = request.form['identifier']
        url = create_presigned_url(identifier)
        return Response(
            BytesIO(requests.get(url).content),
            mimetype='image/jpeg',
            headers={"Content-Disposition": "attachment;filename=" + str(uuid.uuid4())}
        )