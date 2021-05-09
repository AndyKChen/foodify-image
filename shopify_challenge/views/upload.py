import datetime
import os
import time
import uuid
from multiprocessing.pool import ThreadPool

from flask import flash, redirect, render_template, request, session
from flask.views import MethodView

from shopify_challenge.helpers.config import S3_BUCKET_NAME
from shopify_challenge.helpers.decorators import login_required
from shopify_challenge.helpers.s3_helpers import create_presigned_post, upload
from shopify_challenge.models.image import ImageModel


class Upload(MethodView):

    @login_required
    def post(self):
        uploaded_files = request.files.getlist("file")
        private = "private" == request.form.get("access_type")
        presigned_posts = []

        for file in uploaded_files:
            if (file.filename == ""):
                flash("You must select at least one image!", 'danger')
                return render_template("upload.html")
            
            identifier = str(uuid.uuid4())
            image = ImageModel(session['username'],
                               identifier,
                               datetime.datetime.now(),
                               private)
            try:
                image.save_to_database()
            except Exception:
                return {'message': 'An error occurred saving the image to the database.'}, 500

            new_post = create_presigned_post(S3_BUCKET_NAME, identifier)
            presigned_posts.append(new_post)

        pool = ThreadPool(processes=20)
        start = time.time()
        pool.starmap(upload, zip(presigned_posts, uploaded_files))
        end = time.time()
        print(end - start)
        return redirect("/")

    @login_required
    def get(self):
        return render_template("upload.html")

