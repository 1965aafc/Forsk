import random
import os
import time
def hangman():
    for h in hang:
        print(h)
def welcome():
    print("|Welcome to Hangman Game|")
    print("     * To EXIT game - type quit\n     "
          "* The computer will pick a random word and you have to guess the word letter by letter\n     "
          "* You have three lifeline\n     "
          "* It a name of Fruit")

def check(character):                           #Function to check the character in word
    global hang
    global random_word
    global guess_word
    global lifeline
    if character.lower() =='quit':
        return 0
    elif character in random_word and character not in guess_word:
        for index in range(len(random_word)):
            if character == random_word[index]:
                guess_word[index]=character
    else:
        print("Wrong guess")
        if lifeline==5:
            hang.append("\t\t\t (*)")
        elif lifeline==4:
            hang.append("\t\t\t /|\ ")
        elif lifeline==3:
            hang.append("\t\t\t  |  ")
        elif lifeline==2:
            hang.append("\t\t\t / \ ")
        elif lifeline==1:
            hang.append("\t\t\t Dead ")
        time.sleep(1)
        lifeline-=1
    #print("Random Word :",' '.join(guess_word))
    if ''.join(guess_word)==random_word:
        print("You Win !!!")
        return 0

lifeline =5
guess_word=[]
hang =[]
f = open("words.txt","r")
Word_list = f.read().splitlines()                                 #Reading Word list from file
random_word = random.choice(Word_list)                            #selecting random word from list
[guess_word.append("_") for char in random_word]

while lifeline>0:
    os.system('cls')
    welcome()
    print("Random Word :", " ".join(guess_word))
    hangman()
    character = input("Guess letter :").lower()
    x = check(character)
    if x == 0:
        break
else:
    os.system('cls')
    welcome()
    print("Random Word :", " ".join(guess_word))
    hangman()
    print("You Loss !!")
print("Thanks !!!!")
