#!/usr/bin/python

import os
import sys
import boto3
path = "./"
# get an access token, local (from) directory, and S3 (to) directory
# from the command-line
local_directory = '_site/'
bucket = 'noahcover.com'
#destination = 'finance_customers_table/gather_customer_data_repo'

print("Deleting...")
s3 = boto3.resource('s3')
bucketName = s3.Bucket(bucket)
bucketName.objects.filter(Prefix="/").delete()
print( "Done")

client = boto3.client('s3')
client.put_object(
        Bucket=bucket,
        Body='',
        Key='/'
        )
# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    # construct the full Dropbox path
    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = relative_path  #os.path.join(destination, relative_path)

    # relative_path = os.path.relpath(os.path.join(root, filename))
    print("Uploading %s..." % s3_path)
    client.upload_file(local_path, bucket, s3_path)
