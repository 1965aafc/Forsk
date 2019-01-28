#importing libraries
import hashlib
import os
import csv

os.chdir("F:\\College 1st sem\\PYTHON")

#opening the file 
with open('zoo.csv') as zoofile:
    #reading the file
    csvread=csv.reader(zoofile,delimiter=',')
    #
    for x in csvread:
        #using sha1 TO FIND THE HASH OF THE FILE
        z=hashlib.sha1(x[2])
        print z
    
        
