import os
import boto3
import uuid
import time
import requests
from multiprocessing.pool import ThreadPool

from flask import redirect, render_template, session, request
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required

# Initalize s3 client 
s3_client = boto3.client(
    's3',
    aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY'),
    region_name='us-east-2'
)

# Helper function to take post a file to s3 using a presigned url
def upload(presigned_post, file):
    files = [
        ('file', file)
    ]
    http_response = requests.post(presigned_post['url'], data=presigned_post['fields'], files=files)
    return http_response

# Helper function to generate a presigned post
def create_presigned_post(bucket_name, object_name, fields=None, conditions=None, expiration=3600):
    response = s3_client.generate_presigned_post(bucket_name,
                                                 object_name,
                                                 Fields=fields,
                                                 Conditions=conditions,
                                                 ExpiresIn=expiration)
    return response

class Upload(MethodView):

    @login_required
    def post(self):
        uploaded_files = request.files.getlist("file")
        presigned_posts = []
        for file in uploaded_files:
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

