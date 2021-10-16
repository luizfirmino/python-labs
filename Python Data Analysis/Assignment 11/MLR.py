#!/usr/bin/env python3

# Assignment: 3.14 LAB: Multiple Regression
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
from pandas import DataFrame
import statsmodels.api as sm


mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/nbaallelo_slr.csv")

# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(DB_DIR)

df = DataFrame(nba,columns=['opp_pts','elo_i','pts']) 


# Perform multiple linear regression on pts, elo_i, and opp_pts
X = df[['opp_pts','elo_i']]  
Y = df['pts']
X = sm.add_constant(X) # adding a constant

# Code to perform multiple regression using statsmodels ols
results = sm.OLS(Y, X).fit()

predictions = results.predict(X)

print_model = results.summary()
print(print_model)

aov_table = sm.stats.anova_lm(results, typ=2)
print(aov_table)




#print(results.summary())

# Create an analysis of variance table
#aov_table = sm.stats.anova_lm(results, typ=2)

# Print the analysis of variance table
#print(aov_table)


