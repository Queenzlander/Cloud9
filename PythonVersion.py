import sys
print(sys.version)

import boto3
user=()

sts = boto3.client('sts')
try:
    user=sts.get_caller_identity()['UserId']
    print('The users userId is {0}'.format(user))
except boto3.exceptions.ClientError:
    print("Credentials are NOT valid.")
