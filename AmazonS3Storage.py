from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import config as cfg
from boto3.s3.transfer import S3Transfer
import boto3,os,time,sys
import botocore
import base64
import hmac, hashlib


#creating the connection
#Creating your own session
session = boto3.session.Session(aws_access_key_id='AKIAISCR66QIGSTK3TNA', aws_secret_access_key='7Sw7oQQpvLTXwrhsIL3Ov8/oBy7+0m0a2vmBqnP6', region_name='us-west-2')

sqs = session.client('sqs')
s3 = session.resource('s3')
s3 = boto3.resource('s3')
AWS_BUCKET = ('samsybucket')
app = Flask(__name__)
app.debug = False
'''
#creating the bucket

s3.create_bucket(Bucket='SamsonBucket')
s3.create_bucket(Bucket='SamsonBucket',CreateBucketConfiguration = {
    'LocationConstraint':'Oregon'})

'''
'''
@app.route('/')
def WelcomeToLogin():
    return "Welcome to flask"
'''
'''

# authenicating the user
@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['username']
    obj = conn.get_object('mycontainer','names.txt')
    name_list = []
    a = 0
    name_list.extend(obj[1].split())
    for x in name_list:
        if x == text:
            a = 1
    if a == 1:
        return app.send_static_file('index.html')
    else:
        return app.send_static_file('notfound.html'





'''

#upload function
@app.route("/upload", methods=['POST', 'GET'])
def upload():
     uploaded_files = request.files.getlist("files[]")
     for upload_file in uploaded_files:
         session = boto3.session.Session(aws_access_key_id='AKIAISCR66QIGSTK3TNA', aws_secret_access_key='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', region_name='us-west-2')
         sqs = session.client('sqs')
         s3 = session.resource('s3')
         s3 = boto3.resource('s3')
         AWS_BUCKET = ('samsybucket')
         if upload_file and allowed_file(upload_file.filename):
             filename = secure_filename(str(time.time()) + upload_file.filename)
             dir_name = 'uploads/'
             policy = base64.b64encode(policy_document)
             signature = base64.b64encode(hmac.new(AWS_SECRET_ACCESS_KEY, policy, hashlib.sha1).digest())
             if not os.path.exists(dir_name):
                 os.makedirs(dir_name)
                 file_path = os.path.join(dir_name, filename)
                 app.logger.info("Saving file: %s", file_path)
                 transfer = S3Transfer(boto3.client(s3, cfg.AWS_REGION, aws_access_key_id=cfg.AWS_APP_ID,
                                               aws_secret_access_key=cfg.AWS_APP_SECRET))

                 transfer.upload_file(file_path, AWS_BUCKET, file_path)
                 upload_file.save(file_path)
     return render_template('index.html')

#storing the data
bucket= s3.Bucket('samsybucket')
s3.Object('samsybucket','companies.txt').put(Body=open('companies.txt','rb'))
s3.Object('samsybucket','samson.jpg').put(Body=open('samson.jpg','rb'))

#saving the s3 object to file using boto3
s3_client = boto3.client('s3')
#open('companies.txt').write('Hello, world!')

# Upload the file to S3

s3_client.upload_file('companies.txt', 'samsybucket', 'companies-remote.txt')

# Download the file from S3

@app.route("/download", methods=['POST', 'GET'])
def download():
     s3_client.download_file('samsybucket', 'companies-remote.txt', 'companies2.txt')
     print(open('companies2.txt').read())



'''
#accessing the bucket
bucket = s3.Bucket('samsybucket')
exists =True
try:
    s3.metaclient.head_bucket(Bucket='samsybucket')
except botocore.exceptions.ClientError as e:
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
        exists = False

'''
# deleting the bucket
#bucket = s3.Bucket('flaskbucket')
#for key in bucket.objects.all():
    #key.delete()
#bucket.delete('flaskbucket')

# iterating through the bucket
bucket = s3.Bucket('samsybucket')
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)
'''
def main(argv):
    bucket = s3.Bucket('samsybucket')
    isValid=True
    while isValid:
        options = {1: upload, 2: download , 3:exit}
        option = input("Enter your option 1. Upload 2.Download 3. exit")
        if option=="3":
            print "Exiting..\n"
            isValid=None
        else:
            options[option](bucket)
'''
if __name__ == '__main__':
     app.run()
    #main(sys.argv)
    #port = int(os.environ.get('PORT', 5000))app.run()
        
