#------------------------------------------------------------------------------------------------------------------------------------------------------
#       Creator: Sarah Gillespie
#        Date: August 13th, 2019
#    Filename: randomWord.py
# Description: random vocab generator for GRE Questions
#      Github: https://github.com/SarahGillespie/GRE-vocab-multiple-choice
#------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import random
from graphics import *

WIDTH = 800
HEIGHT = 800

def setUp(WIDTH, HEIGHT):
    '''creates and repeats a simple multiple choice quiz ad infinitum'''

    vocabData = pd.read_csv('vocabData.csv')

    #opens and loads the list of vocabulary words.
    with open('vocabData.csv') as csvfile:
        row_count = sum(1 for row in csvfile)
        totalWords = int(row_count) #counts the total number of definitions.
        print(",___,")
        print('[O.o]"')
        print("/)__)")
        print('-"--"-')
        print(" ")
        print("words = ", totalWords)
    score = 0
    total = 0
    
    #creates a main window
    win = GraphWin("Game", 800, 800)

    #black backdrop
    BACKGROUND = Rectangle(Point(0,0), Point(WIDTH, HEIGHT))
    BACKGROUND.setFill("black")
    BACKGROUND.draw(win)

    #sets up the scorebox
    scorebox = Rectangle(Point(HEIGHT - 80,(WIDTH/2 + 20)), Point(HEIGHT,(WIDTH/2 - 20)))
    scorebox.setFill('blue')
    scorebox.draw(win)

    #setting up the placement of each colored box
    placementHEIGHTA = (1/6)*HEIGHT#multiphy by what box it is
    placementWIDTHA = (1/6)*WIDTH

    Box_one = Rectangle(Point(placementHEIGHTA, placementWIDTHA), Point(placementHEIGHTA + 20, placementWIDTHA + 30))  # points are ordered ll, ur
    Box_one.draw(win)
    Box_two = Rectangle(Point(placementHEIGHTA, 2*placementWIDTHA), Point(placementHEIGHTA + 20, 2*placementWIDTHA + 30))
    Box_two.draw(win)
    Box_three = Rectangle(Point(placementHEIGHTA, 3*placementWIDTHA), Point(placementHEIGHTA + 20, 3*placementWIDTHA + 30))
    Box_three.draw(win)
    Box_four = Rectangle(Point(placementHEIGHTA, 4*placementWIDTHA), Point(placementHEIGHTA + 20, 4*placementWIDTHA + 30))
    Box_four.draw(win)
    Box_five = Rectangle(Point(placementHEIGHTA, 5*placementWIDTHA), Point(placementHEIGHTA + 20, 5*placementWIDTHA + 30))
    Box_five.draw(win)

    #definesthe colors for each box
    Box_one.setFill("purple")
    Box_two.setFill("purple")
    Box_three.setFill("purple")
    Box_four.setFill("purple")
    Box_five.setFill("purple")

    #prints the / sign in the scorebox
    divideText = Text(Point(HEIGHT - 60,(WIDTH/2 + 20)),"/")
    divideText.setTextColor("red")
    divideText.setSize(30)
    divideText.draw(win)

    #placeholder for printing the correct word/guestion when you get a question incorrect
    endText = Text(Point((5*6)*HEIGHT,((1/2)*WIDTH))," ")
    endText.setTextColor("red")
    endText.setSize(30)
    endText.draw(win)

    #placeholder for printing the correct definition when you get a question incorrect
    endText2 = Text(Point((5*6)*HEIGHT,((1/2)*WIDTH))," ")
    endText2.setTextColor("red")
    endText2.setSize(30)
    endText2.draw(win)

    #placeholder for printing the correct sentence when you get a question incorrect
    endText3 = Text(Point((5*6)*HEIGHT,((1/2)*WIDTH))," ")
    endText3.setTextColor("red")
    endText3.setSize(30)
    endText3.draw(win)

    #this will loop the game after each question
    repeat = True
    while repeat == True:

        
        #draws the first score of 0
        scoreText = Text(Point(HEIGHT - 80,(WIDTH/2 + 20)),(score))
        scoreText.setTextColor("red")
        scoreText.setSize(30)
        scoreText.draw(win)

        #draws the first total of 0
        totalText = Text(Point(HEIGHT - 40,(WIDTH/2 + 20)),(total))
        totalText.setTextColor("red")
        totalText.setSize(30)
        totalText.draw(win)
        

        #picks a random integer from the total number of words. remember that counting starts at 0
        thisRow = random.randint(0, totalWords)

        #selects and displays the word from the random row as a question.
        question = [vocabData['def'][thisRow]]
        print(question,"?")

        #prints the question
        questionGRAPHIC = Text(Point(HEIGHT/2, WIDTH/9), str(question))
        questionGRAPHIC.setSize(18)
        questionGRAPHIC.setTextColor("red")
        questionGRAPHIC.draw(win)
        
        
        #selects the correct definition
        theDef = vocabData['word'][thisRow]

        #selects the correct sentance
        sent = vocabData['sent'][thisRow]

        #chooses 4 random definitions to make the other muliple choice answers and make this more challenging.
        randomDef1 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef2 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef3 = vocabData['word'][int(random.randint(0, totalWords))]
        randomDef4 = vocabData['word'][int(random.randint(0, totalWords))]

        #creates a list of incorrect definitions, correct definitions, and a list with all definitions.
        wrong = [randomDef1, randomDef2, randomDef3, randomDef4] #list of all the wrong definitions
        correct = [theDef] #list of 1, just the correct definiton
        allChoices = wrong + correct #list of all definitions

        #shuffles/randomizes all definitions
        choices = random.sample(allChoices, len(allChoices))

        #prints each definition to the screen
        choices1GRAPHIC = Text(Point(placementHEIGHTA + 20, placementWIDTHA + 30), str(choices[0]))
        choices1GRAPHIC.setSize(18)
        choices1GRAPHIC.setTextColor("red")
        choices1GRAPHIC.draw(win)

        choices2GRAPHIC = Text(Point(placementHEIGHTA + 20, 2*placementWIDTHA + 30), str(choices[1]))
        choices2GRAPHIC.setSize(18)
        choices2GRAPHIC.setTextColor("red")
        choices2GRAPHIC.draw(win)

        choices3GRAPHIC = Text(Point(placementHEIGHTA + 20, 3*placementWIDTHA + 30), str(choices[2]))
        choices3GRAPHIC.setSize(18)
        choices3GRAPHIC.setTextColor("red")
        choices3GRAPHIC.draw(win)

        choices4GRAPHIC = Text(Point(placementHEIGHTA + 20, 4*placementWIDTHA + 30), str(choices[3]))
        choices4GRAPHIC.setSize(18)
        choices4GRAPHIC.setTextColor("red")
        choices4GRAPHIC.draw(win)

        choices5GRAPHIC = Text(Point(placementHEIGHTA + 20, 5*placementWIDTHA + 30), str(choices[4]))
        choices5GRAPHIC.setSize(18)
        choices5GRAPHIC.setTextColor("red")
        choices5GRAPHIC.draw(win)

        #in the shell, this prints all the definitions on a different line random order.
        for i in choices:
            print(" ")
            print(i)

        typedResponse = win.getKey()
        guess = typedResponse
        
        #if you wanted to use the shell only, then get input via below
        #guess = input("Which definition is this? 1, 2, 3, 4, or 5")

        #converts guess 1 to computer counting of item 0
        guess = (int(guess) - int(1))
        
        #cleans up the corrected definition from the previous question (or the placeholder text from the start)
        endText.undraw()
        endText2.undraw()
        endText3.undraw()

        #ask if [content of shuffled list item that you picked] = [item 0 (our only item) in correct list]
        if choices[guess] == correct[0]:
            scoreText.undraw()
            totalText.undraw()
            
            print("correct!")
            score = score + 1
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
            questionGRAPHIC.undraw()
            choices1GRAPHIC.undraw()
            choices2GRAPHIC.undraw()
            choices3GRAPHIC.undraw()
            choices4GRAPHIC.undraw()
            choices5GRAPHIC.undraw()

            #this prints placeholder text to the shell
            endText = Text(Point((5*6)*HEIGHT,((1/2)*WIDTH))," ")
            endText.setTextColor("red")
            endText.setSize(30)
            endText.draw(win)
        #if your guess is not the same as the answer key    
        elif choices[guess] != correct[0]:
            
            scoreText.undraw()
            totalText.undraw()
            print("wrong answer***")

            #this prints the correct definition to the shell so you can learn for next time
            print(question, ": ", correct[0])
            total = total + 1
            print("SCORE: ",score, "out of ", total)
            print("----------------------------------------------------------------------")
            print(" ")
            questionGRAPHIC.undraw()
            choices1GRAPHIC.undraw()
            choices2GRAPHIC.undraw()
            choices3GRAPHIC.undraw()
            choices4GRAPHIC.undraw()
            choices5GRAPHIC.undraw()

            correctPrintable = str(correct[0])

            #this prints the correct definition to the Zelle graphics window so you can learn for next time
            endText = Text(Point(HEIGHT/2,725), correctPrintable)
            endText.setTextColor("red")
            endText.setSize(30)
            endText.draw(win)

            endText2 = Text(Point(HEIGHT/2,750), question)
            endText2.setTextColor("red")
            endText2.setSize(15)
            endText2.draw(win)

            endText3 = Text(Point(HEIGHT/2,775), sent)
            endText3.setTextColor("red")
            endText3.setSize(15)
            endText3.draw(win)
 

def main():
    setUp(WIDTH,HEIGHT)

    
if __name__ == "__main__":
    main()
