import os

import boto3
from flask import redirect, render_template, session
from flask.views import MethodView


class Discover(MethodView):
    def get(self):

        cloudfront = os.environ.get('CLOUDFRONT_DOMAIN')

        s3_resource = boto3.resource(
            's3',
            aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
            aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
        )
        my_bucket = s3_resource.Bucket(os.environ.get('S3_BUCKET_NAME'))
        summaries = my_bucket.objects.all()

        return render_template('discover.html', my_bucket=my_bucket, files=summaries, cloudfront=cloudfront)