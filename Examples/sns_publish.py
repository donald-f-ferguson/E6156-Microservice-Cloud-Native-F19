import boto3
import json


def publish_it():

    client = boto3.client('sns')

    client.publish(TopicArn="arn:aws:sns:us-east-1:832720255830:E6156CustomerChange",
                   Message='{ "customers_email" : "dff9@columbia.edu"}')

if __name__ == "__main__":
    publish_it()


