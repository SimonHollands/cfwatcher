from os import listdir
from os.path import isfile, join
import os, shutil 
from s3pushpull2 import s3pushpull
import urllib.request
import pandas as pd
import io
import time

s3=s3pushpull()

class Listener:

    def __init__(self, s3_data_key='S3:/breakwater_data/breakwater_data.csv'):
        self.vars=['date','surfer_count']
        self.s3_data_key=s3_data_key
        self.obj=s3.s3.get_object(Bucket='surfcounter14367', Key=s3_data_key)
        self.data = pd.read_csv(io.BytesIO(self.obj['Body'].read()))[self.vars]

    def hit_model(self):
        response = urllib.request.urlopen('http://13.57.217.48/model').read().decode('ASCII')
        new = [{'date':pd.datetime.now(),'surfer_count':int(response)}]
        self.data=self.data.append(pd.DataFrame(new))
        self.count=int(response)
        self.data.to_csv('data/temp.csv')
        s3.upload_aws('data/temp.csv', 'S3:/breakwater_data/breakwater_data.csv')
        print(self.data.head())


# if __name__ == "__main__":
#     listener=Listener()
#     print(listener.data.head())

    # for i in range(100):
    #     listener.hit_model()
    #     print(f'''Smack, {listener.count} surfers right now.''')
    #     time.sleep(60*5)


