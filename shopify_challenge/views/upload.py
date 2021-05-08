import os
import uuid
import time
from multiprocessing.pool import ThreadPool

from flask import redirect, render_template, session, request, flash
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required
from shopify_challenge.helpers.image_upload import upload, create_presigned_post

class Upload(MethodView):

    @login_required
    def post(self):
        uploaded_files = request.files.getlist("file")
        access_type = request.form.get("access_type")
        presigned_posts = []

        for file in uploaded_files:
            if (file.filename == ""):
                flash("You must select at least one image!", 'danger')
                return render_template("upload.html")
            new_post = create_presigned_post(os.environ.get('S3_BUCKET_NAME'), str(uuid.uuid4()))
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

