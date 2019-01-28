# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:37:49 2019

@author: ashwa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:20:23 2019

@author: ashwa

"""

#source;-https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d
#importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


# set the filepath and load in a shapefile
fp = "F:\\forsk\\Day4,5\\District_Boundary.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)

# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()

#plotting the map of the shape file preview of the maps without data in it
map_df.plot()

#opening the csv file which contains the data to be plotted on the map
df = gpd.read_file("F:\\forsk\\Day4,5\\District_Boundary.shp")
df.head()

#selecting the columns required
df = df[['DIST_NAME','POPULATION']]

#renaming the column name

data_for_map = df.rename(index=str, columns={'DIST_NAME': 'DISTRICT',
'POPULATION': 'POP'})

# check dat dataframe
data_for_map.head()

# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('DIST_NAME').join(data_for_map.set_index('DISTRICT'))

#.head() returns the top 5(by default ) lines of the dataframe
merged.head()

# set a variable that will call whatever column we want to visualise on the map
variable = 'POP'
# set the range for the choropleth
vmin, vmax = 120, 220
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))


# create map
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# remove the axis
ax.axis('off')

# add a title
ax.set_title('Population of Rajasthan', fontdict={'fontsize': '25', 'fontweight' : '3'})

# create an annotation for the data source
ax.annotate('Source: Rajasthan Datastore, 2019',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
            
# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# empty array for the data range
sm._A = []
# add the colorbar to the figure
cbar = fig.colorbar(sm)

fig.savefig('map_export.png', dpi=300)            