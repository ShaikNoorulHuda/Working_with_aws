# import boto3

# def create_s3_bucket(bucket_name):
#     # AWS credentials
#     aws_access_key_id = 
#     aws_secret_access_key = 
#     aws_region = 'us-east-1'

#     # Create an S3 client
#     s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

#     # Create the S3 bucket
#     try:
#         s3.create_bucket(Bucket=bucket_name)
#         print(f"S3 bucket '{bucket_name}' created successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Replace 'your_bucket_name' with your desired bucket name
# bucket_name = 'ailogic-4-bucket'
# create_s3_bucket(bucket_name)






# import boto3

# def upload_file_to_s3(file_name, bucket_name):
#     # AWS credentials
#     aws_access_key_id = 
#     aws_secret_access_key = 
#     aws_region = 'us-east-1'

#     # Create an S3 client
#     s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

#     # Upload file to S3 bucket
#     try:
#         with open(file_name, 'rb') as file:
#             s3.upload_fileobj(file, bucket_name, file_name)
#         print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Replace 'your_bucket_name' with your bucket's name and 'your_file_path' with the file you want to upload
# bucket_name = 'ailogic-4-bucket'
# file_path = "C:\\Users\\snoorul\\Downloads\\SPK 2.pdf"

# upload_file_to_s3(file_path, bucket_name)








import requests
import boto3
from botocore.exceptions import ClientError

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def upload_file_to_s3(file_name, bucket_name):
    
    aws_access_key_id = acess_key
    aws_secret_access_key = secret_key
    aws_region = 'us-east-1'

    
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    
    try:
        with open(file_name, 'rb') as file:
            s3.upload_fileobj(file, bucket_name, file_name)
        print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

url = url
file_name = file_name
bucket_name = bucket_name


downloaded_file = download_file(url, file_name)


upload_file_to_s3(downloaded_file, bucket_name)


