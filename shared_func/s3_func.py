import os

def upload_file_to_s3(file_name, bucket_name, object_name=None, region='us-east-1'):
    """
    Uploads a file to an S3 bucket using the AWS CLI and makes it publicly accessible.

    Parameters:
    - file_name (str): The path to the file to upload.
    - bucket_name (str): The name of the S3 bucket.
    - object_name (str, optional): The S3 object name. If not specified, file_name is used.
    - region (str): The AWS region where the bucket is located.

    Returns:
    - str: The public URL of the uploaded file.
    """
    try:
        # If object_name is not specified, use the file_name as the object name
        if object_name is None:
            object_name = os.path.basename(file_name)  # Use just the filename as the object name

        # Construct the S3 path
        s3_path = f"s3://{bucket_name}/{object_name}"

        # Construct the AWS CLI command to upload the file and set its ACL to public-read
        # Add --region parameter to ensure the correct endpoint is used
        command = f"aws s3 cp {file_name} {s3_path} --acl public-read --region {region}"

        # Execute the command using os.system()
        result = os.system(command)

        # Check if the command was successful
        if result == 0:
            # Generate the public URL with the regional endpoint
            public_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"
            print(f"File uploaded successfully. Public URL: {public_url}")
            return public_url
        else:
            print(f"Error uploading file: AWS CLI command failed with exit code {result}.")
            return None

    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

