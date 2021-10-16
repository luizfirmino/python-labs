#!/usr/bin/env python3

# Assignment: 2.6 LAB: Measures of Center
# Author: Luiz Firmino

import os
from os import path
import pandas as pd

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/mtcars.csv")

# read in the file mtcars.csv
df = pd.read_csv(DB_DIR)

# find the mean of the column wt
mean = df["wt"].mean()

# find the median of the column wt
median = df['wt'].median()

# find the mode of the column wt
mode = df['wt'].mode()

print("mean = ", mean, ", median = ", median, ", mode = ", mode)