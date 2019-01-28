
# Web Scraping with BeautifulSoup and Requests

# Parsing the content from the website and 
# pulling  the exact information you want
# Introduce to the page for Web Scrapping 

# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

"""
Introduce the concept of basic HTML tags
HTML
  HEAD
    
  HEAD

  BODY
    
  BODY
HTML

"""

from bs4 import BeautifulSoup
import requests

# Create simple html files and 
# parse that using bs4 to make the students understand with title, div etc

with open("data/simple.html") as html_file :
  soup = BeautifulSoup(html_file, "lxml")
    
print (soup)

print (soup.prettify())

print (soup.title)

print (soup.title.text)

print (soup.div)

print (soup.div.h1.text)

# Crome browser ( use the inspect tool to use the find function )
match = soup.find('div')
print (match)

match = soup.find("div", class_= "footer")
print (match)

print ( match.h2 )
print ( match.h2.text )

print ( match.p )
print ( match.p.text )

for article in soup.find_all("div") :
  headline = article.p.text
  print (headline)

# Give students a challenge to print some information from the HTML pages 




# Reading from the Internet
from bs4 import BeautifulSoup   
source = requests.get("http://httpbin.org/html").text
soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

print (soup.head)

print (soup.body)

print (soup.body.h1)

print (soup.body.div)

print (soup.body.div.p)

print (soup.body.div.p)



# Web Scrapping a real Page 

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
import unicodedata



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
soup = BeautifulSoup(source)



print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)


#Generate lists
A=[]
B=[]    
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].find(text=True)))
        B.append(str(states[1].find(text=True)))
        C.append(str(unicodedata.normalize('NFKD', cells[1].find(text=True)).encode('ascii','ignore')))        
        D.append(str(unicodedata.normalize('NFKD', cells[2].find(text=True)).encode('ascii','ignore')))
        E.append(str(cells[3].find(text=True)))
        F.append(str(unicodedata.normalize('NFKD', cells[4].find(text=True)).encode('ascii','ignore')))



#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame()
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("former.csv")
#print (df)



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


# Add Web Scrapping using Selenium
# pip install selenium


#Download 

#https://www.seleniumhq.org/download/
#installation for firefox
#https://github.com/mozilla/geckodriver/
#installation for chrome
#https://sites.google.com/a/chromium.org/chromedriver/




import pandas as pd
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')
driver = webdriver.Chrome("F:\\forsk\\DAY16\\chromedriver.exe")

driver.get(wiki)    # Opening the submission url



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    states=row.find_elements_by_tag_name("th") #To store second column data
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].text))
        B.append(str(states[1].text))
        C.append(str(unicodedata.normalize('NFKD', cells[1].text).encode('ascii','ignore')))        
        D.append(str(unicodedata.normalize('NFKD', cells[2].text).encode('ascii','ignore')))
        E.append(str(cells[3].text))
        F.append(str(unicodedata.normalize('NFKD', cells[4].text).encode('ascii','ignore')))



#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("former.csv")
#print (df)

driver.quit()



#Real website data scrapping for Kerela Results

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
browser = webdriver.Chrome("F:\\forsk\\DAY16\\chromedriver.exe")
browser.get(url)


sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()





