import boto3
import os

def upload_file_to_s3(file_name, bucket_name, object_name=None, region='us-east-1'):
    """
    Uploads a file to an S3 bucket using boto3 with s33ding profile.
    """
    try:
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Create boto3 session with s33ding profile
        session = boto3.Session(profile_name='s33ding')
        s3_client = session.client('s3', region_name=region)

        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name, 
                             ExtraArgs={'ACL': 'public-read'})

        public_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"
        print(f"File uploaded successfully. Public URL: {public_url}")
        return public_url

    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

