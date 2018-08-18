import time
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#SMSHANGHAI MMSI:371544000
#HYUNDAI JAKARTA: 372561000

# https://services.marinetraffic.com/api/exportvesseltrack/YOUR-API-KEY/v:2/period:value/days:value/mmsi:value

# https://services.marinetraffic.com/api/exportvesseltrack/8205c862d0572op1655989d939f1496c092ksvs4/v:2/period:daily/days:3/mmsi:241486000
API_KEY  = 'e795047356ca4d689602176dba0fdb2b8a618a07'
BASE_URL = 'https://services.marinetraffic.com/api/exportvesseltrack/v:2/'

https://services.marinetraffic.com/api/exportvesseltrack/e795047356ca4d689602176dba0fdb2b8a618a07/v:2/period:daily/days:10/mmsi:372561000/protocol:csv

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



extract_marine_data(BASE_URL, API_KEY, )




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