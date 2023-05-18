import boto3


ec2 = boto3.resource('ec2')

    
instances = ec2.instances.filter(
     Filters = [
          {'Name': 'instance-state-name', 'Values': ['running']},
          {'Name': 'tag:ENV','Values':['Development']}
     ]
)

for instance in instances:
     try:
          instance.stop()
          print(f'{instance} has been put into stopped state')
     except:
          print(f'There are no instances to be stopped')