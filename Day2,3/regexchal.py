#email id validation
import re

#email entered
string='ashwanidhankhar@gmail.com'

#regex format for string validation 
s=re.search(r'^[\w\._]+@[A-Za-z]+\.[a-zA-Z]+$',string)

#printing the matched string
print(s.group())
       
