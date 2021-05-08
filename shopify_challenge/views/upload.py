import os
import boto3
import time
import uuid
from multiprocessing.pool import ThreadPool

from flask import redirect, render_template, session, request
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required

s3_resource = boto3.resource(
    's3',
    aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
)
my_bucket = s3_resource.Bucket(os.environ.get('S3_BUCKET_NAME'))

def upload(file):
    id = str(uuid.uuid4())
    my_bucket.Object(id).put(Body=file)

class Upload(MethodView):

    @login_required
    def post(self):

        uploaded_files = request.files.getlist("new_images")
        pool = ThreadPool(processes=20)
        start = time.time()
        pool.map(upload, uploaded_files)
        end = time.time()
        print(end - start)
        return redirect("/")

    @login_required
    def get(self):
        return render_template("upload.html")

