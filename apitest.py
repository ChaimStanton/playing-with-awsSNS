#!./env/bin/python3

import boto3

client = boto3.client('lambda')

client.invoke(FunctionName = "testInitalLamdaFunction",
              Payload = """
                        {
                        "message": "this is a test from lambda via python yay",
                        "subject": "subject lolls from lambda"
                        }"""
                        )