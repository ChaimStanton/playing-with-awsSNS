#!./env/bin/python3

import boto3
from botocore.exceptions import ClientError

sns = boto3.resource('sns')
topic = sns.Topic('arn:aws:sns:eu-west-1:696210664380:tescoBot')
topic.publish(Message="hey this is a test using the api",
              Subject="test messgae")
