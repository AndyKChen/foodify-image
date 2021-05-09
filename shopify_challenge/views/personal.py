import os

from io import BytesIO

from flask import render_template, session, request, redirect, Response
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required
from shopify_challenge.models.image import ImageModel
from shopify_challenge.helpers.s3_helpers import delete_image, create_presigned_url
from shopify_challenge.helpers.config import CLOUDFRONT
import requests


class Personal(MethodView):
    
    @login_required
    def get(self):
        public_images = ImageModel.get_public_images_by_username(session['username'])
        private_images = ImageModel.get_private_images_by_username(session['username'])
        return render_template("personal.html", public_images=public_images, private_images=private_images, cloudfront=CLOUDFRONT)
    
    @login_required
    def post(self):
        action = request.form.get('action')
        identifier = request.form['identifier']
        image = ImageModel.get_image_by_identifier(identifier)
        if action == "make public" or action == "make private":
            image.change_privacy()
        elif action == "delete":
            delete_image(identifier)
            image.delete_from_database()
        elif action == "download":
            url = create_presigned_url(identifier)
            return Response(
                BytesIO(requests.get(url).content),
                mimetype='image/jpeg',
                headers={"Content-Disposition": "attachment;filename=" + identifier}
            )
        return redirect('/personal')