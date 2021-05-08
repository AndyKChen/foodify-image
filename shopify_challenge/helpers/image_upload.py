# Initalize s3 client 
import os
import boto3
import requests

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