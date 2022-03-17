#!flask/bin/python
#from crypt import methods
from flask import Flask, jsonify, abort, request, make_response, url_for, send_file
from flask import render_template, redirect
import os
import time
import datetime
#import exifread
import json
#import boto3
#import MySQLdb

app = Flask(__name__, static_url_path="")

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=5000)
