# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:16:29 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
"""
#importing lilbraries
import requests
from bs4 import BeautifulSoup
import unicodedata

#url for site site from where data has to be scrapped
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

#getting the data by get function of requests library
source= requests.get(url).text

#using beautiful soup to handle the html from the data
soup=BeautifulSoup(source)

#prettifying the data
soup.prettify()

#finding all the tables present in the webpage
all_tables=soup.find_all('table')

print all_tables

#finding the table from the webpage which has calss = table
tables=soup.find('table',class_='table')

print tables

tables.prettify()

#MAKE LISTS ... making lists where the columns has to be stored 
a=[]
b=[]
c=[]
d=[]
e=[]

#itereating the data from the table
for row in tables.findAll('tr'):
    #finding all the td from the table and storing its data in a variable
    cells=row.findAll('td')
    if len(cells)==5:
        #appending the diiferent colummns in different lists
        a.append(str(cells[0].find(text=True)))
        b.append(str(cells[1].find(text=True)))
        c.append(str(cells[2].find(text=True)))
        d.append(str(cells[3].find(text=True)))
        e.append(str(cells[4].find(text=True)))
        print a,b,c,d,e
        
import pandas as pd

#creating dataframes 
df=pd.DataFrame()
#storing the value stored in the list in the dataframes
df['Position']=a
df['Country']=b
df['Matches']=c
df['Points']=d
df['Rating']=e
#creating a csv from the dataframes
df.to_csv("ODI_RANKING.csv")
