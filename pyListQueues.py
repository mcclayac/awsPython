__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'




import boto3


# Get the service respurce
sqs = boto3.resource('sqs')


# Printe each Queuename, which is part of it's ARN
for queue in sqs.queues.all():
    print(queue.url)


