#!/usr/bin/env python3

# Assignment: 1.12 LAB: Subsetting data frames
# Author: Luiz Firmino

import os
from os import path
import pandas as pd

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/mtcars.csv")

cylinders = int(input())
df = pd.read_csv(DB_DIR)
df_cyl = df[df.cyl == cylinders]
print(df_cyl)