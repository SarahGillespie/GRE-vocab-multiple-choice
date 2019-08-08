———————————————————————————————————RandomWord————————————————————————————————————

RandomWord is a simple multiple choice and text-based game to help me practice vocabulary words for the GRE verbal reasoning section. Currently there are two option: word-focused and definition focused. The word-focused part of RandomWord displays a GRE vocal word and you need to pick the correct definition out of the five options by typing the corresponding number. Definition-focused works the same, but you are provided a definition and guess the word.

If you’ve downloaded the files, you should have everything you need to run the game but may need to install Python and extra packages, including pandas and numpy. Other packages are also imported because I hope to improve the game in the future with a more sophisticated graphics display and graphing your results. The following instructions will allow you to double check that you have all the required files, and will tell you how to run RandomWord.

———————————————————————————————————How to Run RandomWord———————————————————————————
Open the python file ‘randomWord.py’ and select ‘run’ from the menu bar, then ‘run module’. From there the text-based game is displayed in the Python shell that will pop up. Pressing 1, 2, 3, 4, or 5 will select the corresponding answer choice and add points to your score.

———————————————————————————————————Prerequisites———————————————————————————————————

There are a number of items you need to install before running RandomWord.

First, install Python if you haven’t already. This project was built with Python 3, specifically for Mac OS. The graphics may work differently on other platforms. Download Python for Mac OS here: https://www.python.org/downloads/

You may need to install pandas and numpy, both software libraries for data analysis. These read the CSV of words.

Next, the graphics for RandomWord were built with John M. Zelle’s Simple Graphics Library. If you need to install this, download Zelle Graphics “graphics.py” from this website (http://mcsp.wartburg.edu/zelle/python/), and keep the graphics.py file in the same file as randomWord.py

You will need to have downloaded a vocabData.csv and have it in the same file as the game code. These are included with the zip file, so you should already have them.

———————————————————————————————————Known Bugs———————————————————————————————————
Keyboard input other than the given numbers will make the game crash.

Closing the window creates an exception in the Python shell.

Sometimes there is a Pandas error with reading the CSV file. I have not found a solution online yet.

———————————————————————————————————Sources———————————————————————————————————
Words and definitions are sourced from around the web, including Lexico.com (www.lexico.com/en), online Merriam-Webster dictionary (www.merriam-webster.com/), Kaplan website (www.kaptest.com/study/gre/top-52-gre-vocabulary-words/).

Feeling, David and Kotchian, Vince. 6 GRE Practice Tests. Self. 2nd Edition, Barron’s, 2015.

Instructions for Zelle Graphics - Zelle, John. “Graphics Reference (graphics.py v5).” PDF file. http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

———————————————————————————————————Creators———————————————————————————————————
This project was created by Sarah Gillespie as a hobby project over summer 2019. If you have any questions, please reach out to sarahelizabethgillespie@gmail.com.