__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'



# Boto 3
import boto3
s3 = boto3.resource('s3')


data = open('/Users/anthonymcclay/Pictures/atlassian.jpg', 'rb')


# Boto 3
s3.Object('anthony.mcclay.mybucket1', 'atlassian.jpg').put(Body=data)