import boto3
ec2 = boto3.resource('ec2')


instance = ec2.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId='ami-02396cdd13e9a1257',
    InstanceType='t2.micro',
    KeyName='app_ec2',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'EMPinstance'
                },
            ]
        },
    ]
)

print(instance)