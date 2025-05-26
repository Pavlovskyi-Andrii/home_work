ec2 = boto3.client('ec2')
    
# Фільтрація по тегу
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:My_tag', 'Values': ['Andrey']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)
print(response)
# instances_to_stop = []

# for reservation in response['Reservations']:
#     for instance in reservation['Instances']:
#         instances_to_stop.append(instance['InstanceId'])

# if instances_to_stop:
#     ec2.stop_instances(InstanceIds=instances_to_stop)
#     return f"Stopped instances: {instances_to_stop}"
# else:
#     return "No running instances with tag 'AutoStop=true'"