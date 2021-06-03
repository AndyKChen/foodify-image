import os
from io import BytesIO

import requests
from flask import Response, redirect, render_template, request, session
from flask.views import MethodView

from foodify.helpers.config import CLOUDFRONT
from foodify.helpers.decorators import login_required
from foodify.helpers.s3_helpers import (create_presigned_url,
                                                  delete_image)
from foodify.models.image import ImageModel


class Personal(MethodView):
    
    @login_required
    def get(self, page_num):
        public_images = ImageModel.get_public_images_by_username(session['username'], page_num)
        private_images = ImageModel.get_private_images_by_username(session['username'], page_num)
        return render_template("personal.html", public_images=public_images, private_images=private_images, cloudfront=CLOUDFRONT), 200
    
    @login_required
    def post(self, page_num):
        action = request.form.get('action')
        identifier = request.form['identifier']
        image = ImageModel.get_image_by_identifier(identifier)
        if action == "make public" or action == "privatize":
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
            ), 200
        return redirect('/personal/' + str(page_num)), 301