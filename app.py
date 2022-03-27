#!flask/bin/python
#from crypt import methods
from flask import Flask, jsonify, abort, request, make_response, url_for, send_file
from flask import render_template, redirect
import os
import time
import datetime
import exifread
import json
import boto3
import MySQLdb

app = Flask(__name__, static_url_path="")

UPLOAD_FOLDER = os.path.join(app.root_path,'static','media')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
BASE_URL="http://localhost:5000/media/"
AWS_ACCESS_KEY="AKIAV7X5LSUDT5U7CNNI"
AWS_SECRET_KEY="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"
REGION="us-east-1"
BUCKET_NAME="elasticbeanstalk-us-east-1-411774457095"
DB_HOSTNAME="database-1.cd2k4ohtbwvf.us-east-1.rds.amazonaws.com"
DB_USERNAME = 'admin'
DB_PASSWORD = 'SE317Group'
DB_NAME='photos'
#DB_HOSTNAME="photogallery-db.czivfufzq0kh.us-east-1.rds.amazonaws.com"
#DB_PASSWORD = 'CloudyWithAChance422'
#DB_NAME='photogallery'

@app.route('/', methods=['GET', 'POST'])
def home_page():
    conn = MySQLdb.connect (host = DB_HOSTNAME,
                        user = DB_USERNAME,
                        passwd = DB_PASSWORD,
                        db = DB_NAME, 
            port = 3306)
    cursor = conn.cursor ()
    cursor.execute("SELECT * FROM photogallery.photogallery2;")
    results = cursor.fetchall()
    
    items=[]
    for item in results:
        photo={}
        photo['PhotoID'] = item[0]
        photo['CreationTime'] = item[1]
        photo['Title'] = item[2]
        photo['Description'] = item[3]
        photo['Tags'] = item[4]
        photo['URL'] = item[5]
        items.append(photo)
    conn.close()        
    print(items)
    return render_template('index.html', photos=items)

#@app.route('/')
#def hello_world():
#	return 'Hello Worlddd!'

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=5000)
