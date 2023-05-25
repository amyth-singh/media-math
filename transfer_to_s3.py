#%%
import pandas as pd
import gen
import split
import boto3
import time

# Resources
access_key_id = 'AKIASVUN4TFQRNO4CFAO'
secret_access_key = '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'
s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

class Decorators:
    def __init__(self):
        pass

    def run_timer(func):
            def wrapper():
                t1 = time.time()
                func()
                t2 = time.time() - t1
                print(f"{func.__name__} : ran in {t2} seconds")
            return wrapper

class GenFileUpload():
    def __init__(self):
        pass

    @Decorators.run_timer
    def gen_file_to_s3():
        s3_bucket_name = 'mediamath-s3-bucket'
        output_dir = 'source_split_files'
        for i in range(1, 11):
            file_name = f'part-{i}.csv.gz'
            file_path = f'{output_dir}/{file_name}'
            s3.upload_file(file_path, s3_bucket_name, file_name)
            print(f"Uploaded {file_name} to S3 bucket {s3_bucket_name}")
        print("Files uploaded successfully!.")

class GenFileS3Download:
    def __init__(self):
        pass 

    def gen_file_s3_download_link():
        s3_bucket_name = 'mediamath-s3-bucket'
        file_name = 'part-3.csv.gz'
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': s3_bucket_name,
                'Key': file_name
            },
        )
        return url


