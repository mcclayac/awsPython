__author__ = 'anthonymcclay'
__project__ = 'awsPython'
__date__ = '11/8/16'
__revision__ = '$'
__revision_date__ = '$'



import boto3


# Get the service respurce
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='tonynodelayqueue')

# Create a message
response = queue.send_message(MessageBody='Hello Message World')

# Print message meta-data
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))


queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})


response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'These Nutz'
    },
    {
        'Id': '2',
        'MessageBody': 'taste Good',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])



print("\n\nMessage Sent")


