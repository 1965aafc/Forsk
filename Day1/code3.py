#importing libraries

import csv

#creating an emoty dictionary
dict1={}

#opening the text file
with open('text.txt')as text:
    #reading the file with ':' separation
    read=csv.reader(text,delimiter=':')
    for x in read:
        #ignoring the line if the line starts with # 
        if(x[0]=="#"):
            continue
        #Adding the lines to a dictionary which contains first field as username and 3 field as the password in text file.
        else:
            dict1[x[0]]=int(x[3])

#printing the vlaues from dictionary 
for keys,values in dict1.items():
    print keys,"=",values
        
