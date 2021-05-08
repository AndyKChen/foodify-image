import os
import boto3

from flask import redirect, render_template, session, request
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required


class Upload(MethodView):

    @login_required
    def post(self):

        uploaded_files = request.files.getlist("new_images")

        cloudfront = os.environ.get('CLOUDFRONT_DOMAIN')

        s3_resource = boto3.resource(
            's3',
            aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
            aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
        )
        my_bucket = s3_resource.Bucket(os.environ.get('S3_BUCKET_NAME'))

        for file in uploaded_files:
            my_bucket.Object(file.filename).put(Body=file)
        return redirect("/")

    @login_required
    def get(self):
        return render_template("upload.html")

