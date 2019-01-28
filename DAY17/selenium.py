# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:17:38 2019

@author: ashwa
"""

from selenium import webdriver
import requests
from time import sleep
from bs4 import BeautifulSoup as BS


url="https://www.google.com/"

browser = webdriver.Chrome("F:\\forsk\\DAY16\\chromedriver.exe")

browser.get(url)


sleep(2)

code=browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

code.click()

sleep(5)

code1="ashwani"

code.send_keys(code1)

search=browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')

search.click()