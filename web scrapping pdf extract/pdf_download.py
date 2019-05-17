# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:50:02 2019

@author: ashwa
"""

from selenium import webdriver
import requests
from time import sleep
from bs4 import BeautifulSoup as BS
from selenium.common.exceptions import NoSuchElementException
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


for x in range(417):
    download_app=browser.find_element_by_xpath('//*[@id="application_action_container"]/div/div/div[1]/a[2]/img')
    download_app.click()
    sleep(3)
    next_pg=browser.find_element_by_xpath('//*[@id="nextPage"]')
    next_pg.click()


