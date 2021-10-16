#!/usr/bin/env python3

# Assignment: 2.7 LAB: Standard Deviation
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import scipy.stats as st
import numpy as n

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/NBA2019.csv")

#'''Type your code here to load the csv file NBA2019.csv.'''
NBA2019_df = pd.read_csv(DB_DIR)

# Input desired column. Ex: AGE, 2P%, or PointsPerGame.
chosen_column = str(input("Which collunm you need the standard deviation from: "))

# Create subset of NBA2019_df based on input.
NBA2019_df_column = NBA2019_df[[chosen_column]]

# Find standard deviation and round to two decimal places. 
sample_s = st.tstd(NBA2019_df_column)
sample_s_rounded = n.round(sample_s, 2)

# Output
print('The standard deviation for', chosen_column, 'is', sample_s_rounded)

