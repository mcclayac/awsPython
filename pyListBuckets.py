__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'



import boto3

for bucket in boto3.resource('s3').buckets.all():
    print(bucket.name)

