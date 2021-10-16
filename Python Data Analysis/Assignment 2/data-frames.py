#!/usr/bin/env python3

# Assignment: 1.11 LAB: Data Frames
# Author: Luiz Firmino
import os
from os import path
import pandas as pd

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "cars.csv")

cars_df = pd.read_csv(DB_DIR)
userNum = int(input())

# Subset the first userNum rows of the data frame
car_df = cars_df[cars_df.Quality == userNum]

print(car_df.max())