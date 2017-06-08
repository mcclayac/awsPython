__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'




import boto3, pprint

client = boto3.client('ec2')

# response = client.describe_regions(
# RegionNames=[
#         'us-west-1',
#     ]
# )
#
# pprint.pprint(response)




response = client.describe_regions()

pprint.pprint(response)