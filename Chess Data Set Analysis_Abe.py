# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:21:14 2022

@author: Abrah
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import rcParams
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

## LIBRARIES TO TRY ##
# https://altair-viz.github.io/
# https://docs.bokeh.org/en/latest/docs/gallery.html
# https://python-chess.readthedocs.io/en/latest/
##

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 9,7


###############################################################################
### CLEAN UP DATA
###############################################################################

# column names, without the chess moves column
misc_columnNames = ['PNG_File_Pos - DELETE ME', 'Date of Game', 'Game Result', 'W-ELO', 'B-ELO', 
                    'Num Moves', 'miscDate - DELETE ME', 'result - DELETE ME', 'wELO - DELETE ME', 'bELO - DELETE ME', 
                    'event date - DELETE ME', 'setup - DELETE ME', 'fen - DELETE ME', 'flag - DELETE ME', 'oyrange - DELETE ME', 
                    'bad len - DELETE ME']

# read all data except chess moves,
misc_chess_data = pd.read_csv('https://raw.githubusercontent.com/abecsumb/DataScienceProject/main/Chess_Data.txt', comment = '#', infer_datetime_format = True, header = None, sep = ' ', on_bad_lines = 'skip')
misc_chess_data.drop(misc_chess_data.columns[16], axis = 1, inplace = True)
misc_chess_data.columns = misc_columnNames

# Isolate game moves from everything else.
game_moves = pd.read_csv('https://raw.githubusercontent.com/abecsumb/DataScienceProject/main/Chess_Data.txt', sep = '###', on_bad_lines = 'skip', header = None)

# drop first column of game moves (this is the misc chess data)
game_moves.drop(game_moves.columns[0], axis = 1, inplace = True)

# split game moves df into columns for each move. 
game_moves = game_moves.iloc[:, 0].str.lstrip()
game_moves = game_moves.iloc[:].str.split(pat = ' ', expand = True)

# merge misc data and game moves into one df, and drop all unnecessary columns
chess_data = pd.concat([misc_chess_data, game_moves], axis = 1)
chess_data.drop(labels = ['PNG_File_Pos - DELETE ME', 'miscDate - DELETE ME', 'result - DELETE ME', 
               'wELO - DELETE ME', 'bELO - DELETE ME', 'event date - DELETE ME', 
               'setup - DELETE ME', 'fen - DELETE ME', 'flag - DELETE ME', 'oyrange - DELETE ME', 'bad len - DELETE ME'], axis = 1, inplace = True)


# remove rows with missing player ratings. Only the players playing as Black had their ELO missing.
chess_data = chess_data[chess_data['B-ELO'] != 'None']

# remove rows where the number of game moves is 0.
chess_data = chess_data[chess_data['Num Moves'] != 0]

# we only want games with openings that we can analyze, so get all games that 
# have num moves at least 16 (8 move each side)
chess_data = chess_data[chess_data['Num Moves'] >= 16]



# we only care about the year that the game took place. reformat the date col to reflect that.           < ---------- HOW DO I DO THIS?
# try a string function on the df.

#example, 
new_column = chess_data['Date of Game'].str.slice(0, 4, 1)
chess_data['Date of Game'] = new_column

###############################################################################
### PRELIM DATA ANALYSIS
###############################################################################

# consider the opening as the first 8 moves (each side).
openings_white = chess_data.loc[:, 0: 15: 2] 
openings_black = chess_data.loc[:, 1: 16: 2] 

# consider the endgame to be the point at which there are a total of 12 pieces or less on the board.

def foofunc(x):
    x['tempCol'] = 'this is a temp col, delete later'
    return x

endgamesIndex = foofunc(chess_data)


# i want this function to search the dataframe game moves for the character 
# 'x', which means a piece was taken, and return the num pieces left.
# 
def countPiecesTaken(x):
    numPieces = 32
    # if the char x is detected in move, reduce numPieces by one.
    
    if (numPieces <= 12)
        return numPieces 

# modify the countPiecesTaken function so that the function returns when there are 12 pieces or less.


## THIS IS HOW YOU ACCESS EACH CHAR
chess_data.loc[4, 0][-2]  # this will get the second to last string char in each move column






def calc_sum(x):
  return x.sum()

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

df = pd.DataFrame(data)

x = df.apply(calc_sum)

print(x)
