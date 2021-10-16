#!/usr/bin/env python3

# Assignment: LAB 3.13 : Creating Correlation matrices
# Author: Luiz Firmino

import os
from os import path
import numpy as np
import pandas as pd
import statsmodels.formula.api as sms

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/nbaallelo_slr.csv")


# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(DB_DIR)

# Display the correlation matrix for the columns elo_i, pts, and opp_pts
print(pd.DataFrame(nba,columns=['elo_n','pts','opp_pts']))

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts']

# Display the correlation matrix for elo_i and y

print(pd.DataFrame(nba,columns=['elo_n','y']))
