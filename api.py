import flask
from flask import request, jsonify
from flask import send_file
import urllib.request
import os   
import time 
import datetime
#######
##Description for the app
#######
from flask import render_template
from flask import Flask, request, url_for, redirect, render_template

from flask import Flask
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler


from listen.listen import Listener
listener=Listener()


app = flask.Flask(__name__)
scheduler = BackgroundScheduler()
crawl_count=0

def fetch_data_from_api():
    '''
     Do your job here
    '''
    print("Iam Fetching now")
    listener.hit_model()
    return redirect(url_for('home'))

@app.route('/')
def home():
    message=str(datetime.datetime.now())
    return render_template('index.html',message=message)

if __name__ == '__main__':


    #add your job here 
    #app.run(threaded=False,use_reloader=False, host="0.0.0.0", port=80)

    app.run(threaded=False,use_reloader=False)
