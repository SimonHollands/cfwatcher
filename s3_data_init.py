from os import listdir
from os.path import isfile, join
import os, shutil 
from s3pushpull2 import s3pushpull
import urllib.request
import pandas as pd
import datetime
s3=s3pushpull()

x_init=pd.DataFrame([{'date':pd.datetime.now(),'surfer_count':3}])
x_init.to_csv('init.csv')
s3.upload_aws('init.csv', 'S3:/breakwater_data/breakwater_data.csv')

