import os
import csv
import re

words=0
os.chdir("F:\\forsk\\Day2\\novels")
"""

with open("james_joyce_ulysses.txt","rt") as novel:
    read=csv.reader(novel,delimiter=" ")
    for x in read:
        words+=len(x)
print words


                                #OR

words=0
os.chdir("F:\\forsk\\Day2\\novels")

novel= open("james_joyce_ulysses.txt","rt")
for x in novel:
    split1=x.split()
    words+=len(split1)
print words

"""
                               #OR
novel= open('james_joyce_ulysses.txt')
x=novel.read().lower()
    
word=re.findall(r'\w+',x)
z=len(word)
print "The number of words in novel ulysses are =",z


#2 the different number of words in novel ulysses are
words=set(word)
print len(words)


#3
n=0
novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']
while(n<len(novels)):
    novel= open(novels[n])
    x=novel.read().lower()
    result=re.search(r'^[START OF]',x)
    print result
    word=re.findall(r'\w+',result)
    z=len(word)
    print "The number of words in novel",novels[n],"are =",z
    words=set(word)
    print "The number of distinct words in novel",novels[n],"are =",len(words),"\n"
    n+=1

