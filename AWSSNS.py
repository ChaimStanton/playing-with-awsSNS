#!./env/bin/python3

import boto3
from botocore.exceptions import ClientError
import datetime

sns = boto3.resource('sns')
topic = sns.Topic('arn:aws:sns:eu-west-1:696210664380:tescoBot')
topic.publish(Message="hey this is a test using the api sent at " + str(datetime.datetime.now()),
              Subject="test messgae")
