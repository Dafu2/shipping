import time
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta



API_KEY  = '06259c8703c98a577f33405e9fe6b8f689e345c7'
BASE_URL = ''
target_date = datetime(2016, 5, 16) 
features=[]

def extract_marine_data(url, api_key, target_date, days):  
    records = []
    for _ in range(days):
        request = BASE_URL.format(API_KEY, target_date.strftime('%Y%M%D'))
        response = request.get(request)
        if response.status_code == 200:
            data = response.json()['history']['dailysummary'][0]
            records.append(DailySummary(

            ))
            time.sleep(60)
            target_date += timedelta(days=1)
        else:
            print("Bad response.")



# def extract_weather_data(url, api_key, target_date, days):  
#     records = []
#     for _ in range(days):
#         request = BASE_URL.format(API_KEY, target_date.strftime('%Y%m%d'))
#         response = requests.get(request)
#         if response.status_code == 200:
#             data = response.json()['history']['dailysummary'][0]
#             records.append(DailySummary(
#                 date=target_date,
#                 meantempm=data['meantempm'],
#                 meandewptm=data['meandewptm'],
#                 meanpressurem=data['meanpressurem'],
#                 maxhumidity=data['maxhumidity'],
#                 minhumidity=data['minhumidity'],
#                 maxtempm=data['maxtempm'],
#                 mintempm=data['mintempm'],
#                 maxdewptm=data['maxdewptm'],
#                 mindewptm=data['mindewptm'],
#                 maxpressurem=data['maxpressurem'],
#                 minpressurem=data['minpressurem'],
#                 precipm=data['precipm']))
#         time.sleep(6)
#         target_date += timedelta(days=1)
#     return records