# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:32:23 2019

@author: ashwa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:22:11 2019

@author: ashwa
"""


#source:--https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#to import the basemap library give the direct path to the library 
import os
os.environ["PROJ_LIB"]="C:\\Users\\ashwa\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap
import geopandas as gpd


city=gpd.read_file("F:\\forsk\\Day4,5\\District_Boundary.shp")

csv=pd.read_csv("F:\\forsk\\Day10\\Day10 Rajasthan\\latlong_raj.csv")

lat=csv['LAT'].values
lon=csv['LONG'].values
population = city['POPULATION'].values
dist=city['DIST_NAME'].values

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=27.0238, lon_0=74.2179,
            width=1.05E6, height=1.2E6)
m.shadedrelief()

m.drawcoastlines(color='blue',linewidth=3)
m.drawcountries(color='gray',linewidth=3)
m.drawstates(color='gray')

# scatter city data, with c reflecting population
m.scatter(lon,lat, latlon=True,
          c=population,s=700,
          cmap='YlGnBu_r', alpha=0.5)
#create colorbar 
plt.colorbar(label=r'Population')
plt.clim(300000, 4000000)


dict1={}
list1=[]
list2=[]
list3=[]
n=0
#storing each value in different lists
for z in lat:
    list1.append(z)
for c in lon:
    list2.append(c)
for b in dist:
    list3.append(b)
#storing the values of lat long in a dictionary with lat as keys and long as values    
while(n<len(list1)):
    dict1[list1[n]]=list2[n]
    n+=1
    
i=0
# Map (long, lat) to (x, y) for plotting
#naming the cities of Rajasthan with the help of their lat(z)long(c)
for z,c in dict1.items():
    x,y = m(c, z)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y,list3[i], fontsize=10);
    i+=1