# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:11:51 2019

@author: ashwa
"""

from selenium import webdriver
import requests
from time import sleep
from bs4 import BeautifulSoup as BS
import os

url="https://internshala.com/"

options= webdriver.ChromeOptions()
options.add_experimental_option("prefs",{"download.default_directory":"F:\\forsk\\PDF extract\\PDF\\"})

browser = webdriver.Chrome("F:\\forsk\\DAY16\\chromedriver.exe",chrome_options=options)

browser.get(url)


sleep(2)

login=browser.find_element_by_xpath('//*[@id="register-button-positioner"]/button')

login.click()

sleep(5)

employer=browser.find_element_by_xpath('//*[@id="modal_employer"]')

employer.click()

sleep(2)

email=browser.find_element_by_xpath('//*[@id="modal_email"]')

email.click()

id="info@forsk.in"

email.send_keys(id)

passs=browser.find_element_by_xpath('//*[@id="modal_password"]')

passs.click

password="Forsk@jpr19"

passs.send_keys(password)

login=browser.find_element_by_xpath('//*[@id="modal_login_submit"]')

login.click()

sleep(2)

view_app=browser.find_element_by_xpath('//*[@id="view_application_id"]')

view_app.click()

sleep(5)

full_app=browser.find_element_by_xpath('//*[@id="individual_application_20441566"]/div[5]/div[3]/div[2]/div[2]/div[2]/a/button')

full_app.click()

sleep(2)

name=list()
location=list()
phone=list()
college=list()




for x in range(417):
    name_t=browser.find_element_by_class_name('applicant_name').text
    location_t=browser.find_element_by_class_name('applicant_locations').text
    phone_t=browser.find_element_by_class_name('phone_primary').text
    college_t=browser.find_element_by_xpath('//*[@id="prefilled-education-details-table"]').text.split("\n")[1]
    name.append(name_t)
    location.append(location_t)
    phone.append(phone_t)
    college.append(college_t)
    sleep(3)
    next_pg=browser.find_element_by_xpath('//*[@id="nextPage"]')
    next_pg.click()
    sleep(3)
    
   


import pandas as pd

#creating dataframes 
df=pd.DataFrame()
#storing the value stored in the list in the dataframes
df['Name']=name
df['City']=location
df['College']=college
df['Phone Number']=phone
#creating a csv from the dataframes
df.to_csv("Students.csv")
    


