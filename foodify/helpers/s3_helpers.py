# Initalize s3 client 
import os

import boto3
import requests

from .config import ACCESS_KEY_ID, S3_BUCKET_NAME, SECRET_ACCESS_KEY

s3_client = boto3.client(
    's3',
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = SECRET_ACCESS_KEY,
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

# Helper function to delete an image from s3
def delete_image(key):
    s3_client.delete_object(Bucket=os.environ.get('S3_BUCKET_NAME'), Key=key)

# Helper function to generate presgined url for download
def create_presigned_url(key):
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': S3_BUCKET_NAME, 'Key': key},
        ExpiresIn=300
    )
    return url