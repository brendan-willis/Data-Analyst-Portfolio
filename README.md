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

### Project 4 - Optimal Schedule 
This group project consisted of two parts. The first part was to create an optimal schedule for 60 professors based on their course and time preferences and adhering to several constraints. All of the constraints are explained in more detail in the presentation file in the above folder; but one example is that a proffessor could not be scheduled to teach all five days of the week. The second part of this project is to take the schedule and enact changes that need to be made so that it minimized how much the overall schedule is changed. Again, this is all explained in more detail in the folder above. The python code we wrote to generate the schedule can be seen in file '456project2.ipynb'. I had a hand in this code but my biggest contribution to this project was cleaning the data. The project all depended on making a schedule that optimized the professors' time and course preferences. The original data set can be seen in the 'preference_data3' file above. This data set was not even close to the format we needed to write our program. In the 'time_preferences.rmd' file you can see how I cleaned and transformed the data so that we could work with it. The original data we got just had professors rank whether they like teaching early, middle or late in the day on a scale from 1-3. For our program we needed the ranking to be for each hour of each day and on a scale from 0-1. My code takes the original data set and puts it in this format so that we could work with it. The final report for this project is rather lengthy but at the end of it you can find our results. Our code successfully generated a schedule that seemed to maximize each professor's preferences while adhering to all of the constraints.     





