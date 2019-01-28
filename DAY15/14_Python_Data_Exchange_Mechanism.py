# Data Exchange Mechanism 
# Javascript Object Notation (JSON)

"""

JSON has become popular method for exchange of structured information over a 
network and sharing information across platforms.

It is basically text with some structure and saving it as .json

It stores data as key:value pairs.
Anything before : is called key and after : is called value.

This is very similar to Python dictionaries

You can see that the data are separated by , and that curly braces define objects.

Square brackets are used to define arrays in more complex JSON files

Other data types supported are string , number , boolean and null 

encoding is for writing data to disk ( serialisation )

decoding is for reading data into memory ( deserialisation ) 

The process of encoding JSON is usually called serialization.

Naturally, deserialization is the reciprocal process of decoding data that
 has been stored or delivered in the JSON standard.

Think of it like this: encoding is for writing data to disk, 
while decoding is for reading data into memory.

The following table is used to do a conversion from JSON Data types to Python Data Types

Python          JSON
dict            object  { }
list            array   [  ]
str             string  "  "
int             number  89, 98.67
True            true    true
False           false   false 
None            null    null


"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""


# Loading raw json data into python specific data 
import json
##code challenge

data={
	"students": {
		"student1": {
			"firstname": "Dushyant",
			"lastname": "khichi",
			"email": "mailondushyant@gmail.com",
			"phone": [{
				"mobile": "1234567890",
				"phone": "2134567890"
			}],
			"department": "machine learning"
		},
		"student2": {
			"firstname": "Ashwani",
			"lastname": "dhankhar",

			"contact details": [{
				"mobile": "1234321321",
				"phone": "2134542540",
				"email": "ashwanidhankahr@gmail.com"

			}],
			"department": "machine learning"
		}
	},
	"faculties": {
		"faculty1": {
			"firstname": "MR.bablu",
			"lastname": "pandit",
			"contact deatails": [{
				"mobile": "9123832443",
				"phone": "2397647823",
				"email": "lion_of_mirzapur@kaaleen_bhaiya.com"
			}],
			"department": "jhandu gun"
		},
		"faculties": {
			"faculty1": {
				"firstname": "MR.guddu",
				"lastname": "pandit",
				"contact deatails": [{
					"mobile": "9132314323",
					"phone": "2397234324823",
					"email": "lion_of_mirzapur@kaaleen_bhaiya.com"
				}],
				"department": "mirzapur"
			}
		}
	}
}

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
print (type(json_string))

# Converts  JSON Data types to Python Data Types 
my_data = json.loads(json_string)

print (type(my_data) )  # its a python dictionary  , it uses the table to convert 
print (my_data) 
print (my_data['researcher'])

print (my_data['researcher']['relatives'])

print (my_data['researcher']['relatives'][0])

print (my_data['researcher']['relatives'][0]['name'])



# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)
print (type(new_json_string) )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2 )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)
print (new_json_string)



# Writing/Storing the JSON data in a File 

with open("data/data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    # json.dump(json_string, write_file, indent=2   )


# Reading from a JSON file

with open("data/data_file.json", "r") as write_file:
    jsondata=json.load(write_file)
    print(jsondata)
 
    # JSON in python data structure 
    my_data = json.loads(jsondata)
    print ( my_data)
    