#!/usr/bin/env pyhton3.6

import random
import getpass


def getWordsOnline():
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("""This program reqiuires the BeautifulSoup module
        Please install it  from https://pypi.python.org/pypi/beautifulsoup4
        You can also install the module with $ pip install beautifulsoup4
        """)
        exit()

    try:
        import requests
    except ImportError:
        print("""This program reqiuires the Requests module
        Please install it  from https://pypi.python.org/pypi/requests
        You can also install the module with $ pip install requests
        """)
        exit()


    print("Fetching nouns from http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx")

    r = requests.get("http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx")

    print("Fetched page")

    page = BeautifulSoup(r.text,"html5lib")  

    noun_table = page.find("table",{"id":"GridView3"})
    noun_body = noun_table.find("tbody")

    nouns = []

    noun_a = []

    for tr in noun_body.find_all("tr"):
        td = tr.find_all("td")[1]

        if td.find("a") != None:
                noun_a.append(td.find("a"))
        else:
            noun_a.append(td)

    for a in noun_a:
        nouns.append(a.string)

    print("Extracted nouns\n")

    return nouns

guessed_letters = []

def obfuscateWord():
    ob_word = ""

    for l in word:
        ob_word += l if l in guessed_letters else "_"
    
    return ob_word


def checkWin():
    for l in word:
        if not l in guessed_letters:
            return False
    return True

# Hangman --------------------------------------


# SETUP

print("Hangman v0.1")
input_accept = False

while not input_accept:
    query = input("How do you want a word to be randomly selected? [y/n]: ")
    if(query.lower() == "y"):
        noun_list = getWordsOnline()
        word = noun_list[random.randint(0,len(noun_list)-1)]
        input_accept = True
    elif(query.lower() == "n"):
        word = getpass.getpass("Select the word to guess (What you type will not be visible): ")
        input_accept = True
    else:
        print("Input not accepted, try again.")
accept_hp = False
while not accept_hp:
    try:
        hp = int(input("Input HP: "))
        if(hp <= 0):
            print("HP can't be negative or zero")
        else:
            accept_hp = True
    except ValueError:
        print("Input not accepted!")
    except Exception as e:
        print("Something went very wrong :(")
        print("Exception:",e.message)

# PLAY

while True:
    guess = None
    accept = False
    while not accept:
        guess = input("Guess a letter: ").lower()
        if(len(guess) != 1):
            print("ONE letter")
        else:
            accept = True

    if guess in word:
        print("Correct!")
        if guess not in guessed_letters:
            guessed_letters.append(guess)
        if checkWin():
            print("You guessed all the letters! You win!")
            break
    elif hp == 1:
        print("Game Over!")
        break
    else:
        hp -= 1
        print("Wrong!")
    print("What you have guessed so far:",obfuscateWord())
    print("You have {0} lives left\n".format(hp))

print("The word was \"{0}\"".format(word))