# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:12:31 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
import json

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"


url=url1+url2+url3

print url

response=requests.get(url)

print response.content

type(response.content)

json_data=response.json()

for key,values in json_data.items():
    print key,"-->",values,"\n"


json_data["sys"]["sunset"]

json.dumps(json_data)





"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.pyhow to display seaborn.barplot in python3
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests

user=input("enter the USD :")

url= "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y"

responses=requests.get(url)

responses.content

jsondata=responses.json()

inr=jsondata["USD_INR"]["val"]

convert=inr*user

print "Current rate  of 1USD to INR is : {}".format(inr)

print "{} USD to INR = Rs.{}".format(user,convert)