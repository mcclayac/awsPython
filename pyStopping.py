__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'





import boto3, pprint

ec2 = boto3.resource('ec2')

ids = ['i-0078697e1dc01519a', 'i-0bf8720b3321679e3',
       'i-034cd39e79e6cd5f8','i-0018efce280d2b9d2']

ec2.instances.filter(InstanceIds=ids).stop()



