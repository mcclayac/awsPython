__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'


import boto3


# Get the service respurce
sqs = boto3.resource('sqs')


# Create the Queue.  Returns an SQSQueue instance
queue = sqs.create_queue(QueueName='tonynodelayqueue')


# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# /Users/anthonymcclay/.virtualenvs/awsPythonEnv/bin/python /mcclayac/pythoncode/awsPython/pyCreateQueue.py
# https://queue.amazonaws.com/722234550817/test
# 5
#
# Process finished with exit code 0
