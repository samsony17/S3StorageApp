import boto
import boto.s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
import time

def get_bucket(access_key_id, secret_access_key, bucket_name):
    conn = boto.connect_s3('AKIAJRF3WNPREH2OB22Q','Wz54JFbk64BPm1PltwAnOf7eqQuWu44CoX5bsnN' )
    return conn.get_bucket('flaskbucket')

s3 = boto.connect_s3()
#bucket = s3.create_bucket('amrishawss3',location=boto.s3.connection.Location.DEFAULT)
_Local_File_Path='samson.jpg'
_Download_Location_Path='Samson.jpg'


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def upload(bucket):
    k = Key(bucket)
    k.key = 'flaskbucket/samson.jpg'
    print "Uploading..\n"
    starttime = time.time();
    k.set_contents_from_filename(_Local_File_Path,cb=percent_cb, num_cb=10)
    endtime = time.time();
    timetoupload = endtime - starttime;
    print "File uploaded"
    print "Time taken to upload file %f seconds" %timetoupload
    
def download(bucket):
    print "Downloading..\n"
    k1=bucket.get_key('flashbucket/Samson.jpg')
    starttime1 = time.time();
    k1.get_contents_to_filename(_Download_Location_Path,cb=percent_cb, num_cb=10)
    endtime1 = time.time();
    timetodownload = endtime1 - starttime1;
    print "File downloaded"
    print "Time taken to download file %f seconds" %timetodownload

def main(argv):
    bucket = s3.get_bucket('flaskbucket')
    isValid=True
    while isValid:
        options = {1: upload, 2: download , 3:exit}
        option = input("Enter your option 1. Upload 2.Download 3. exit")
        if option=="3":
            print "Exiting..\n"
            isValid=None
        else:
            options[option](bucket)

if __name__ == '__main__':
    main(sys.argv)
