#This program contains functions to scrap post code of a restaurant based on its physical location

import googlemaps
from datetime import datetime

#Googlemap API Key
gmaps = googlemaps.Client(key='AIzaSyAUs9yC6G7b8M5XkJ_FFedlS3d_YI6EGeM')

# Read the restaurant locations information from excel, it's in the nineth sheet and sixth column
import xlrd
data = xlrd.open_workbook('ProtoType_final_v0.1.xlsx')
table = data.sheets()[8]
location = table.col_values(5)[1:]

#  to Geocode an address, first find out the data structure
##for i in location:
##    geocode_result = gmaps.geocode(i)
##    print(geocode_result)

# Find the position of postal code and extract
l1 = []
for i in location:
    geocode_result = gmaps.geocode(i)
    l1.append(geocode_result[0].get('address_components')[-1].get('long_name'))
    #print(l1)

# Write the post code of restaurant into document   
with open ('restaurant postcode information.txt','wt') as wtf:
    for i in l1:
        wtf.write(str(i)+'\n')
