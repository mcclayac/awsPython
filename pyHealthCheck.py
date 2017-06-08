__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'




import boto3, pprint

ec2 = boto3.resource('ec2')


for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    pprint.pprint(status)


