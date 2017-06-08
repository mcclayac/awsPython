__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'


# Boto 3
import boto3
s3 = boto3.resource('s3')

s3.create_bucket(Bucket='anthony.mcclay.mybucket1', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})



