#!/c/Users/dferguso/Python37/python

import argparse
import boto3
import json


def run_it():
    parser = argparse.ArgumentParser(description='Create an SNS Topics')
    parser.add_argument('--name', metavar='topic_name', type=str,
                       help="'Name of the topic to create.'")
    parser.add_argument('--display_name', metavar="'Some cool topic display name.'",
                       help='Seriously?')

    args = parser.parse_args()

    print("Args = ", args)

    client = boto3.client('sns')

    response = client.create_topic(Name="E6156Boo")

    print("Result = ", json.dumps(response, indent=2))

if __name__ == "__main__":
    run_it()

