import argparse
import os
import boto3

def create_cloudformation_stack(base_name, instance_count):
    """
    Create a CloudFormation stack with a LaunchTemplate and Auto Scaling Group.

    Args:
        base_name (str): The base name to use for the created resources.
        instance_count (int): The desired number of instances in the Auto Scaling Group.
    """
    cf = boto3.client('cloudformation')

    with open('cloudformation-template.yaml', 'r') as file:
        template = file.read()

    stack_name = f"{base_name}-stack"
    parameters = [
        {'ParameterKey': 'DesiredCapacity', 'ParameterValue': str(instance_count)}
    ]

    cf.create_stack(
        StackName=stack_name,
        TemplateBody=template,
        Parameters=parameters
    )

    print(f"Created CloudFormation stack: {stack_name}")

def main():
    parser = argparse.ArgumentParser(description='Create CloudFormation resources')
    parser.add_argument('-n', '--name', type=str, required=True, help='Base name for the created resources')
    parser.add_argument('-s', '--size', type=int, required=True, help='Number of instances in the Auto Scaling Group')
    args = parser.parse_args()

    create_cloudformation_stack(args.name, args.size)

if __name__ == "__main__":
    main()
