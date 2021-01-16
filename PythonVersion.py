import sys
print(sys.version)

import boto3
sts = boto3.client('sts')
try:
    sts.get_caller_identity()
    print("Credentials are valid.")
except boto3.exceptions.ClientError:
    print("Credentials are NOT valid.")
    