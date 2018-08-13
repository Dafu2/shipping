import os
from netCDF4 import Dataset
import csv

data_path = '/Users/Xiao/Desktop/warp_gate/shipping/data/NOAA/ICOADS/ICOADS_R3.0.0_2010-01.nc'
extraction_path ='/Users/Xiao/Desktop/warp_gate/shipping/data/NOAA/ICOADS/201001_extracted_dates.csv'

# print (dataset.file_format)
# print (dataset.dimensions.keys())
# print (dataset.dimensions['DATE_len'])
# print (dataset.variables.keys())
# print (dataset.variables['lat'])
# print (dataset.variables['lon'])
# print (dataset.variables['WW'])

print('#####################')
# print (dataset['date'][1])
# print (dataset['date'][1][0:4])
# print (dataset['date'][1][4:6])
# print( dataset['date'][1][6:])



def extract_date(dataset, step):
    date = dataset['date'][step]
    year = dataset['date'][step][0:4]
    month = dataset['date'][step][4:6]
    day = dataset['date'][step][6:]
    print (date)

def check_directory(path):
    for r, d, f in os.walk(path):
        for file in f:
            if ".nc" in file:   
                data_path = ('/Users/Xiao/Desktop/warp_gate/shipping/data/NOAA/ICOADS/%s' % file)
                # print (data_path)
                dataset = Dataset(data_path)
                for x in dataset['date'][0]:
                    extract_date(dataset, x)
                print(file)

check_directory('/Users/Xiao/Desktop/warp_gate/shipping/data/NOAA/ICOADS/')
