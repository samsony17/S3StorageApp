import os
import boto3
from flask import render_template,request
from flask import Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'



@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='GET':
        return render_template('index.html')

@app.route('/ValidateUser',methods=['POST'])
def authenticate():
    if request.method=='POST':
        username=request.form['username']
        auth_files='names.txt'
        os.chdir('/home/samson/Documents')
        f = open(auth_files,'r')
        for line in f.read().split('\n'):
            if (line==username):
                return render_template('/index.html')
            else:
                status='false'
        status_message='Inavlid username'
        if status=='false':
            return """
            <!doctype html>
            <title>Status</title>
            <h1 style="color: #ff0000">%s</h1>
            """ % status_message

@app.route('/List',methods=['GET'])
def List():
    s3=boto3.resource('s3')
    my_bucket=s3.Bucket('samsybucket')
    listfileshtml=''
    for name in my_bucket.objects.all():
        listfileshtml = listfileshtml+"<tr>"
        listfileshtml=listfileshtml+"<td>"+name.key+"</td>"
        listfileshtml=listfileshtml+"</tr>"

    listfileshtml = "<table>"+listfileshtml+"</table>"
    return """
    <!doctype html>
    <title>Files List</title>
    <h1>%s</h1>
    """ % listfileshtml


@app.route('/Download',methods=['GET','POST'])
def Download():
    if(request.method=='POST'):
        print 'Inside the POST Function'
        print os.getcwd()
        s3=boto3.resource('s3')
        client = boto3.client('s3')
        filename=request.form['DownloadFile']
        print filename
        client.download_file('samsybucket', filename, filename)
        status=open(filename).read()
        status='Document Downloaded'
        return """
         <!doctype html>
            <title>Success Status</title>
            <body>%s</body>
            """ % status

@app.route('/Upload',methods=['GET','POST'])
def Upload():
    if request.method == 'POST':
        file=request.files['fileupload']
        filename=file.filename
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        print(os.getcwd())
        print filename
        s3_client=boto3.client('s3')
        s3=boto3.resource('s3')
        data=file.read()
        s3.Bucket('samsybucket').put_object(Key=filename,Body=data)
        status=">Uploaded successfully"
    return """
            <!doctype html>
            <title>Success Status</title>
            <h1%s</h1>
            """ % status

#delete function

@app.route('/Delete',methods=['GET','POST'])
def Delete():
    if(request.method=='POST'):
        print 'Inside the POST Function'
        print os.getcwd()
        s3=boto3.resource('s3')
        client = boto3.client('s3')
        filename=request.form['DeleteFile']
        print filename

        status='Document Deleted'
        return """
         <!doctype html>
            <title>Success Status</title>
            <body>%s</body>
            """ % status


if __name__ == '__main__':
    app.debug = True
    app.run()
