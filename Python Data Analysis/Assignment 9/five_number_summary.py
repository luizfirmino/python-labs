#!/usr/bin/env python3

# Assignment: 2.8 LAB: Five number summary
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import scipy.stats as st
import numpy as n

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/internetusage.csv")

#'''Type your code here to load the csv file NBA2019.csv.'''
df = pd.read_csv(DB_DIR)

# subset the column internet_usage
internet = df[['internet_usage']]

# find the five number summary
five_num = internet.describe()

print(five_num)

