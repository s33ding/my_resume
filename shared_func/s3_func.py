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

        # Determine content type
        content_type = 'application/octet-stream'
        if file_name.endswith('.html'):
            content_type = 'text/html'
        elif file_name.endswith('.css'):
            content_type = 'text/css'
        elif file_name.endswith('.js'):
            content_type = 'application/javascript'
        elif file_name.endswith('.png'):
            content_type = 'image/png'
        elif file_name.endswith('.pdf'):
            content_type = 'application/pdf'

        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name, 
                             ExtraArgs={'ACL': 'public-read', 'ContentType': content_type})

        public_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"
        print(f"File uploaded successfully. Public URL: {public_url}")
        return public_url

    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

def sync_folder_to_s3(local_folder, bucket_name, s3_prefix="", region='us-east-1'):
    """
    Syncs a local folder to S3 bucket, uploading only missing files.
    """
    try:
        session = boto3.Session(profile_name='s33ding')
        s3_client = session.client('s3', region_name=region)
        
        # Get existing S3 objects
        existing_keys = set()
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
            for obj in page.get('Contents', []):
                existing_keys.add(obj['Key'])
        
        uploaded_count = 0
        for root, dirs, files in os.walk(local_folder):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, local_folder)
                s3_key = f"{s3_prefix}/{relative_path}".replace("\\", "/") if s3_prefix else relative_path.replace("\\", "/")
                
                # Skip if file already exists in S3
                if s3_key in existing_keys:
                    continue
                
                # Determine content type
                content_type = 'application/octet-stream'
                if file.endswith(('.pdf', '.PDF')):
                    content_type = 'application/pdf'
                elif file.endswith(('.png', '.PNG')):
                    content_type = 'image/png'
                elif file.endswith(('.webp', '.WEBP')):
                    content_type = 'image/webp'
                
                s3_client.upload_file(local_path, bucket_name, s3_key,
                                    ExtraArgs={'ACL': 'public-read', 'ContentType': content_type})
                print(f"Uploaded: {s3_key}")
                uploaded_count += 1
        
        print(f"Sync completed: {uploaded_count} new files uploaded to s3://{bucket_name}/{s3_prefix}")
        return True
        
    except Exception as e:
        print(f"Error syncing folder: {e}")
        return False

