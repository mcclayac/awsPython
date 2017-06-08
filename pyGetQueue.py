__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'



import boto3


# Get the service respurce
sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

print(queue.url)
print(queue.attributes.get('DelaySeconds'))


