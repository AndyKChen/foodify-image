import os
import uuid
from io import BytesIO

import boto3
import requests
from flask import Response, redirect, render_template, request, session
from flask.views import MethodView

from shopify_challenge.helpers.config import CLOUDFRONT
from shopify_challenge.helpers.s3_helpers import create_presigned_url
from shopify_challenge.models.image import ImageModel


class Discover(MethodView):
    def get(self, page_num):
        images = ImageModel.get_all_public_images(page_num)
        return render_template('discover.html', images=images, cloudfront=CLOUDFRONT)

    def post(self, page_num):
        identifier = request.form['identifier']
        url = create_presigned_url(identifier)
        return Response(
            BytesIO(requests.get(url).content),
            mimetype='image/jpeg',
            headers={"Content-Disposition": "attachment;filename=" + str(uuid.uuid4())}
        )