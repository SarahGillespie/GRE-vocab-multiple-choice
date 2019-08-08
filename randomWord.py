#GRE Questions - random vocab generator
#Sarah Gillespie
#Github repository:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
#from graphics import *
import time

vocabData = pd.read_csv('vocabData.csv')

#below opens and loads the list of vocabulary words.
with open('vocabData.csv') as csvfile:
    row_count = sum(1 for row in csvfile)
    #print(row_count if row_count else 'Empty')
    totalWords = int(row_count) #counts the total number of definitions.
    print(",___,")
    print('[O.o]"')
    print("/)__)")
    print('-"--"-')
    print(" ")
    print("words = ", totalWords)
##############################################################################
def quizWord():
    #we start counting the score at 0. 
    score = 0 #It will increase each time you answer correctly.
    total = 0
    while score < 25:

        print("QUESTION ", total)
        
        #df.loc[row,column] <-- format of how you pull out a cell
        #below picks a random row from the list

        thisRow = random.randint(0, totalWords)

        #remember that counting starts at 0

        WordNumber = vocabData['id'][thisRow]
        WordNumber = int(WordNumber)

        #selects and displays the word
        question = [vocabData['word'][thisRow]]
        print(question,"?")

        #selects the correct definition
        theDef = vocabData['def'][thisRow]
        
        #chooses 4 random definitions to make it confusiong
        randomDef1 = vocabData['def'][int(random.randint(0, totalWords))]
        randomDef2 = vocabData['def'][int(random.randint(0, totalWords))]
        randomDef3 = vocabData['def'][int(random.randint(0, totalWords))]
        randomDef4 = vocabData['def'][int(random.randint(0, totalWords))]
        
        wrong = [randomDef1, randomDef2, randomDef3, randomDef4] #list of all the wrong definitions
        correct = [theDef] #list of 1, just the correct definiton
        allChoices = wrong + correct #list of all definitions

        choices = random.sample(allChoices, len(allChoices)) #shuffles all the definitons

        for i in choices:
            print(" ")
            print(i)#prints the definitions. Each on a different line, in a random order, and with a space before the next.

        #user inputs her guess of which definition matches the random word.
        print(" ")
        guess = input("Which definition is this? 1, 2, 3, 4, or 5")
        guess = (int(guess) - int(1)) #converts guess 1 to computer counting of item 0
        
        #fun scoring part
        #if [content of shuffled list item that you picked] = [item 0 (our only item) in correct list] then you get points
        if choices[guess] == correct[0]:
            print("correct!")
            score = score + 1
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
            
        elif choices[guess] != correct[0]:
            print("wrong answer***")
            print(question, ": ", correct[0])#this prints the correct definition so you can learn for next time
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
def quizDef():
    #we start counting the score at 0. 
    score = 0 #It will increase each time you answer correctly.
    total = 0
    while score < 25:

        print("QUESTION ", total)
        
        #df.loc[row,column] <-- format of how you pull out a cell
        #below picks a random row from the list

        thisRow = random.randint(0, totalWords)

        #remember that counting starts at 0

        WordNumber = vocabData['id'][thisRow]
        WordNumber = int(WordNumber)

        #selects and displays the word
        question = [vocabData['def'][thisRow]]
        print(question,"?")

        #selects the correct definition
        theDef = vocabData['word'][thisRow]
        
        #chooses 4 random definitions to make it confusiong
        randomDef1 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef2 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef3 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef4 = vocabData['word'][int(random.randint(0, totalWords))]
        
        wrong = [randomDef1, randomDef2, randomDef3, randomDef4] #list of all the wrong definitions
        correct = [theDef] #list of 1, just the correct definiton
        allChoices = wrong + correct #list of all definitions

        choices = random.sample(allChoices, len(allChoices)) #shuffles all the definitons

        for i in choices:
            print(" ")
            print(i)#prints the definitions. Each on a different line, in a random order, and with a space before the next.

        #user inputs her guess of which definition matches the random word.
        print(" ")
        guess = input("Which definition is this? 1, 2, 3, 4, or 5")
        guess = (int(guess) - int(1)) #converts guess 1 to computer counting of item 0
        
        #fun scoring part
        #if [content of shuffled list item that you picked] = [item 0 (our only item) in correct list] then you get points
        if choices[guess] == correct[0]:
            print("correct!")
            score = score + 1
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
            
        elif choices[guess] != correct[0]:
            print("wrong answer***")
            print(question, ": ", correct[0])#this prints the correct definition so you can learn for next time
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
            
if __name__ == "__main__":
#    quizWord()
    quizDef()
