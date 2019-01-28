# Program to check Best novel 
"""
Best best novel is that which have max unique Words
"""
import os
import re

os.chdir("F:\\forsk\\Day2\\novels")

# List of novels txt file name
novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

#List to store all words of different noven in multi-dimensional list
novel_wordlist =[]

#list to store number of unique word in novels
unique_wcount = []

#Loop to remove all (special char , white space , digits) and to store in list
for novel in novels:
    file = open(novel,'r')
    filecontent = file.read()
    result = re.search(r'START OF',filecontent)
    startindex = filecontent.find('\n',result.end())
    result = re.search(r'END OF',filecontent)
    filecontent = filecontent[startindex:result.start()]
    filecontent= re.sub("[^a-zA-Z]"," ",filecontent)
    novel_wordlist.append(filecontent.strip().split())
    unique_wcount.append(len(set(filecontent.strip().split())))
    
#finding index of bext novel with max unique word
index = unique_wcount.index(max(unique_wcount))
best = novel_wordlist[index]
x=set(best)
y=set(best)

#To remove all the words in best novel which are comman in other novels
for novel in novel_wordlist:
    if best!=novel:
        x=set(x)-set(novel)
    #To store all comman words from all novels
    y = set(y)&set(novel)
# Storing All unique words in text file
file = open("unique_wword_in_best_novel.txt",'w')
file.write(str(x))
#Here is your Best novel
print("\n\nBest novel is",novels[index] ,"with :-")
print("Total words :",len(novel_wordlist[index]))
print("Unique Words:",unique_wcount[index])
print("Unique Words in this novel form all:",len(x))
print("Total Comman Words in All Novel :",len(y))
