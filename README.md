Make sure that your AWS profile points to an IAM role which has required permissions:
- Create and update cloudformation stack
- VPC full access to create VPC, Subnets, Security Groups
- EC2 access to create ASGs and Launch Templates

Run the Python script with the required parameters:
python create-resources.py -n my-app -s 2


The script will create a CloudFormation stack with the specified base name and number of instances.

You can also add the -h or --help parameter to the script to display a helpful usage message:
