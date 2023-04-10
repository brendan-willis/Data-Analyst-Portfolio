# Data Analyst Portfolio
## Introduction
My name is Brendan Willis and I am currently a senior at the University of Massachusetts Amherst. I will be graduating in May with a degree in Mathematics and concentrations in statistics and actuarial science. I also have an economics minor.

As a Mathematics major, I have taken several classes involving data analysis. Telling stories with data and learning about different things through analysis is a passion of mine. I have analyzed data on Python, R, and Stata and am confident I could quickly pick up any other software. This repository is meant to display some of the projects I have completed in school.

Enjoy!

## Projects

### Project 1 - Data Wrangling
This small project displays my ability to wrangle and clean data on R. I used the 'covidcast' package on R to query over data and pull out observations I was interested in. In this case I pulled out covid data for counties near where I live between 2020 and 2022. I then made some interactive tables to investigate covid rates in these places. Then, I pulled out data for all counties in the United States in the month of January 2022, so I could make an interactive table with the county from each state with the max covid rate from that month. This project isn't so much about getting results from the data; its main purpose is to display my ability to work with data on R. 

### Project 2 - Word Game
This project consists of 3 parts: 
1) Making simple word game.
2) Programming computer player for word game by utilizing monte carlo simulation.
3) analyzing results of simulation.

The initial creation of the word game is contained in the file 'ps2.py' above. When this program is run it deals a hand of 15 random letters to the player. The player makes as many words with the letters as they can until they either run out of letters or can't make any more words. The goal is to score as many points as possible. The 'ps3a.py' contains the second part of this project. This program implements a computer player for the word game that uses monte carlo simulation in order to take N samples from the hand and choose the word that provides the best score. The third part of the project in the file 'ps3c.ipynb' runs the simulation for different values of N. This file displays histograms that show how the score gotten by the computer program tends to increase as N increases.

### Project 3 - SQL on Python
In this project I utilize the sqlite3 library on Python to connect to databases and write SQL queries that clean and filter tables in order to get the data I want. I then use the pandas library to read tables into python as dataframes. I also join\merge tables based on specific columns.





