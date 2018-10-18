# This program contains functions to scrap transportation data for houses from Google Map 

import googlemaps
from datetime import datetime
import json
import xlrd

# Googlemap API Key
gmaps = googlemaps.Client(key='AIzaSyBqui1uHaY4XjhJNUDLjIyU8yiiPbeOS_w')

# Read the house location information from excel, it's in the forth sheet and third column
data = xlrd.open_workbook('ProtoType_final_v0.1.xlsx')
table = data.sheets()[3]
location = table.col_values(2)[1:]

# Before get two spots' distance, first find out the data structure, using normal commute time
time = datetime(2018,10,25,hour=8)
##for m in location:
##    directions_result = gmaps.directions(m,
##                                     "Torrens Buidling, 220 Victoria Square, Adelaide SA 5000",
##                                     mode=i,
##                                     departure_time=time)
##        print(directions_result)

# Notice there are four type of transportation method, drive, walk, bicycle and transit, get each of them seperately
model=['driving', 'walking', 'bicycling', 'transit']
##for m in location:
##    for i in model:
##        directions_result = gmaps.directions(m,
##                                     "Torrens Buidling, 220 Victoria Square, Adelaide SA 5000",
##                                     mode=i,
##                                     departure_time=time)
##        print(directions_result)

# Find the position of how long it takes to transport to destination
##for m in location:
##    for i in model:
##        directions_result = gmaps.directions(m,
##                                     "Torrens Buidling, 220 Victoria Square, Adelaide SA 5000",
##                                     mode=i,
##                                     departure_time=time)
##        print(i+":"+directions_result[0].get('legs')[0].get('duration').get('text'))

#  Find the correct value, extract them
resultl=[]
for m in location:
    for i in model:
        directions_result = gmaps.directions(m,
                                     "Torrens Buidling, 220 Victoria Square, Adelaide SA 5000",
                                     mode=i,
                                     departure_time=time)
        resultl.append(i+":"+directions_result[0].get('legs')[0].get('duration').get('text'))

# write the time required for commuting into document
with open("test_google_map_v0.1.txt","w") as op:
    for i in resultl:
        #op.write(str(i)+'\n')
        op.write(json.dumps(i)+'\n')
        
