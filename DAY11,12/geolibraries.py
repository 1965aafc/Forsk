# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:34:05 2019

@author: ashwa
"""

# Nessecary Imports
import matplotlib.pyplot as plt
import os
os.environ["PROJ_LIB"]="C:\\Users\\ashwa\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap
# Make the figure
plt.figure(figsize=(14, 14))
# Initialize the basemap
m = Basemap(llcrnrlat = 30,
            llcrnrlon = -126,
            urcrnrlat = 45,
            urcrnrlon = -114,
           resolution='h')
# Get the area of interest imagery
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)
# Draw the coasts
m.drawcoastlines(color='b', linewidth=3)
# Draw the states
m.drawstates(color='r',linewidth=3)


import pandas as pd
import numpy as np
# Read in data on all cities
cities = pd.read_csv("F:\\forsk\\DAY11,12\\uscitiesv1.4.csv")
# Choose only cities in california
cities = cities.loc[cities.state_id == 'CA',:]
# Get all the data from the dataframe
lat, lon = cities['lat'], cities['lng']
population,density = cities['population'], cities['density']
# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population),s= 10*np.log(density),
            cmap='viridis', linewidth=0, alpha= .4)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)
# make a guide for the user
for density in [1, 50//3, 50]:
    plt.scatter([], [], c='k', alpha=0.3, s=5*np.log(density),
                label='10* log('+str(density) + ')')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Density')
# add a title
plt.title('California Cities: Density and Population');



#making both the maps together
# Nessecary Imports
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# Make the figure
plt.figure(figsize=(14, 14))
# Initialize the basemap
m = Basemap(llcrnrlat = 30,
            llcrnrlon = -126,
            urcrnrlat = 45,
            urcrnrlon = -114,
           resolution='h')
# Get the area of interest imagery
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)
# Draw the coasts
m.drawcoastlines(color='blue', linewidth=1)
# Draw the states
m.drawstates(color='red',linewidth=3)
m.scatter(lon, lat, latlon=True,
          c=np.log10(population), s=10*np.log(density),
          cmap='Reds', alpha=0.5)
# 3. create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)


#satellite real time data
def make_folder_name(localtime):
    
    if localtime.tm_hour > 12:
        string = str(localtime.tm_mon)+'_'+str(localtime.tm_mday)+'__'+ str(localtime.tm_hour-12)+'-'+str(localtime.tm_min)+'_pm'
    
    else:
        string = str(localtime.tm_mon)+'_'+str(localtime.tm_mday)+'_'+ str(localtime.tm_hour)+'-'+str(localtime.tm_min)+'_am'
    return string
import zipfile
import requests
import time
#names of the datasets and their respective links
names = ['24hrModis1km','48hrModis1km','7dModis1km']
links = ['https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_USA_contiguous_and_Hawaii_24h.zip',
        'https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_USA_contiguous_and_Hawaii_48h.zip',
        'https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_USA_contiguous_and_Hawaii_7d.zip']
folder_names = []
localtime = time.localtime(time.time())
# Save the data into the right spot
# Go through each and  link
for i,name_Link in enumerate(zip(names,links)):
    
    # download the file contents in binary format
    r = requests.get(name_Link[1])
# open method to open a file on your system and write the contents
    with open(name_Link[0], "wb") as code:
        code.write(r.content)
    # Unzip the data
    zip_ref = zipfile.ZipFile(name_Link[0], 'r')
    name = make_folder_name(localtime)+'_'+name_Link[0]
    folder_names.append(name)
    zip_ref.extractall(name)
    zip_ref.close()

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import shapefile
from geopy.geocoders import Nominatim
geolocator = Nominatim()
plt.figure(figsize=(14, 14))
m = Basemap(llcrnrlat = 30,
            llcrnrlon = -126,
            urcrnrlat = 45,
            urcrnrlon = -114,
           resolution='h')
print('fetching image')
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)
# Draw the states
m.drawstates(color='orange',linewidth=1)
print('adding indicators')
names2 = ['MODIS_C6_USA_contiguous_and_Hawaii_24h','MODIS_C6_USA_contiguous_and_Hawaii_48h','MODIS_C6_USA_contiguous_and_Hawaii_7d']
i = 1
for name,name1 in (zip(reversed(folder_names),reversed(names2))):
    shpFilePath = name+'/'+name1
    listx=[]
    listy=[]
    test = shapefile.Reader(shpFilePath)
    for sr in test.shapeRecords():
        x,y = (sr.shape.points[0])
        listx.append(x)
        listy.append(y)
    x,y = m(listx,listy)
    if i == 1:
            Color = 'r'
            Label = '24h Infrared anomalies'
            a = .6
            m.plot(x, y, 'o',color = Color, markersize=10,alpha = a,label=Label)
    if i == 2:
        Color = 'b'
        Label = '48h Infrared anomalies'
        a = .5
        m.plot(x, y, 'o',color = Color, markersize=8,alpha = a,label=Label)
    if i == 3:
        Color = 'g'
        Label = '7d Infrared anomalies'
        a = .2
        m.plot(x, y, 'o',color = Color, markersize=6,alpha = a,label=Label)
        
    i = i + 1
    plt.legend()