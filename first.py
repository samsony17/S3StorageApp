import boto
import boto.s3.connection
access_key = 'AKIAJRF3WNPREH2OB22Q'
secret_key = 'Wz54JFbk64BPm1PltwAnOf7eqQuWu44CoX5bsnN'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'ec2-54-200-160-49.us-west-2.compute.amazonaws.com',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
