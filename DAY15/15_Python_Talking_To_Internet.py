"""
How the HTTP Protocol Works 
TCP/IP was invented in 1983 ( kahn )
world wide web was invented in 1989 ( tim bernes lee )

Communication over the Internet requires the HTTP protocol understanding 
HTTP is a Language to communicate over the internet 
HTTP = Hyper Text Transfer Protocol 
Set of rules that governs how two devices should communicate 
HTTP is a plain text protocol, that means messages sent are in plain text 
HTTP is a stateless protocol
No record of previous interaction and each interaction is processed only with the information that comes with a that particular interaction 
Self Destructing notes which are destroyed after read

How do we converse with a family or friend over a phone
They follow a set of convention ( rules )
You Call
You say Hello
Once Person asks question 
Other response back the question asked 
Then Goodbye
Hang Up 

If two machine talk to one another they need to have more specific tules

Tim Bernes Lee proposed www ( world wide web ) they proposed the first language draft of HTTP (0.9)  in 1991

Introduce the Client and the Sever concept 

Introduce the concept of Request and Response concept 


Introduction to the tool telnet
	HTTP is a plain text protocol, that means messages sent are in plain text 
	Telnet is a tool for Connecting and communicating with a remote device 
	
	Imagine  Server is a house with a unique address and that IP Address 
	This house has a lot of tenants living and each with a specific door for its room
	All the tenants speak a different language ( Hindi, English, Japanese etc )
	HTTP (80) , SMTP (25) , FTP ( 21 ) 

	telnet httpbin.org 80 and press enter once
	GET / HTTP/1.1 and press enter once ( This is know as the  REQUEST line )
	Host: httpbin.org and press enter twice ( Uniform Resource Identifier )
	CTRL + ]
	telnet>quit
	

	Discuss about the response from the server ( HTML )

	telnet httpbin.org 80 
	GET /xml HTTP/1.1  ( This is know as the  REQUEST line )
	Host: httpbin.org and press enter twice   

	Discuss about the response from the server ( XML )

	telnet httpbin.org 80
	GET /forsk HTTP/1.1 
	Host: httpbin.org and press enter twice  


	Fine tuning your request by sending some additional data 

	telnet httpbin.org 80
	GET /get?firstname=Sylvester&language=English HTTP/1.1 
	Host: httpbin.org and press enter twice  
 
	Introduce the concept of Query String 
 
	telnet httpbin.org 80
	GET /get?company=Forsk&city=Jaipur HTTP/1.1 
	Host: httpbin.org and press enter twice  




Format of the HTTP Request 
	
1	Request-Line	GET|POST [uri] HTTP/[version]	GET /xml HTTP/1.1

	GET is for viewing any resource on the server
	POST are used for making a change or updating 

	
2   	Header	[Header Name]: [Header Value]	Host: httpbin.org
										User-Agent: telnet	
										Accept-Language: en-US

3	Blank Line
	
4	Request Body
(optional, only for POST)
( also known as payload)



Format of the HTTP Response 

1	 Status-Line	HTTP/[version] [status code] [status message]	HTTP/1.1 200 OK

100 means Informational Messages 
200 means all OK ( success messages ) 
301 means  ( Resouce requested is moved to different location from the servo )
404 means not found ( Something went wrong in client request ) 
500 means Server Errors ( Something went working on server side while processing the request ) 

2	Headers		[Header Name]: [Header Value]	Server: nginx
											Date: 
											Content-Type: application/xml

3	 Blank Line

4	Response Body	[payload]					XML or HTML						



How to send data using the POST method of HTTP protocol 
	
	telnet httpbin.org 80
	POST /post HTTP/1.1 
	Host: httpbin.org
	Content-Length: 32 and press enter twice for blank line
	
	firstname=Chris&language=English
     	and press enter to send the command 


 
	telnet httpbin.org 80
	POST /post HTTP/1.1 
	Host: httpbin.org
	Content-Length: 30 and press enter for blank line

	firstname=Chris&language=English  	and press enter to send the command 

"""


"""

REST API Basics

REST is another layer on top of HTTP
When u r building a website / App you are building an UI for Apps logic and data model
API is to create a programatic interface or a code UI for same Logic and Data Model
All communication is done through HTTP
API = Application Programming Interface
REST = Representational State Transfer Protocol
Give the story of the Ola / Uber App Interfaces 


/api/v1/games?order=desc&sort=points

this would give back the games in descending order and sorted by points

Header information in request is a very important piece of information 

Request Headers
Accept 
specifies the file format the requester wants
Accept-Language
specifies the human readable language like English , Spanish or Russian
Cache-Control
specifies wether the response can be generated from a cache


Response Header 
Content-Type: text/javascript
Last-Modified: Tue, 15 Nov 2012 12:45:26 GMT
Expires: Thu, 01 Dec 2012 16:00:00 GMT
Status: 200 OK

Explain all the status codes 1xx, 2xx, 3xx, 4xx, 5xx


Endpoint = Specific URI 
Nouns and Verbs ( actions ) needs to be focused 
 
Endpoint points to a single record or a collection of records

/api/v1/games   ( represents a collection of games )
/api/v1/games/1234 ( represents a single games )
/api/v1/1234/games ( this is a wrong approach )

/api/v1/player
/api/v1/players/567


HTTP Methods  used in REST API
GET
is used for fetching either a collection of resources or a single resource.
POST
is used to add a a new resource to a collection
We would POST to /player or /players to crate a new player or game
PUT
is used when we want to update a record. We would not PUT on collection 
DELETE
is used for sending a DELETE request to a detail record, 
a URL for a single record should delete just that record. 
Sending DELETE to an entire collection would delete the whole collection 
but thats usually not implemented with good reason


Rate Limiting Concept of API
 Helps in DDOS 


API Authentication using API Token concept 
Pair A and Pair B keys are being used



++++++++++++++++++++++++++++++++++++++



Introduce to the concept of Web Services ( REST API ) using openweathermap.org


http://api.openweathermap.org/data/2.5/weather?q=Jaipur

http://api.openweathermap.org/data/2.5/weather?q=Jaipur&appid=e9185b28e9969fb7a300801eb026de9c


# if you hit the URL in the browser and try to visualise the JSON, you will come to see that it has 12 items in the object 
# copy and paste this on json lint and visualise 

# coord as Object
#lon as Number
# lat as Number
# weather as List
[ # id as Number
# main as String
# description as String
# icon as String
]
# base as String
# main as Object 
# temp as Number
# pressure as Number
# humidity as Number
# temp_min as Number
# temp_max as Number
# visibility as Number
# wind as Object
# speed as Number
# deg as Number
# clouds as Object
# all as Number
# dt as Number
# sys as Object
# type as Number 
# id as Number
# message as Number
# country as String
# id as Integer
# name as String
# cod as Number



how to parse the response of a HTTP request which is in JSON format.

http://jsonplaceholder.typicode.com/
http://httpbin.org 
https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json
"""



# Get me the temperature of the city from the openweathermap.org

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

print (response.text)
print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))

for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


# Content in binary form
print (type(response.content))

print ("Content or Response Body : " + str(response.content))


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
# response has the original JSON String
# jsondata has the convert string in the python data type dictionary

print ((type(jsondata)))

print (jsondata)

print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
jsondata["main"]["temp"]


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

"""
Code Challenge
  Name: 
    Posting of Data
  Filename: 
    httpbin.py
  Problem Statement:
    Create a client REST API that sends and receives some information from 
    the Server by calling server's REST API.
    You are expected to create two functions each for Sending and 
    Receiving data.
    You need to make two api calls, one with POST method for sending data 
    and the other with GET method to receive data
    All the communication i.e. sending and receiving of data with the 
    server has to be in JSON format
  Hint:
    Host: httpbin.org
    Port :  80
    Protocol : POST
    URI : /post
    Content-Length: 30 

    firstname=Chris&language=English
"""


