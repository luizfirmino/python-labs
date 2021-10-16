#!/usr/bin/env python3

# Assignment: 2.8 LAB: Five number summary
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf 

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/nbaallelo_slr.csv")

# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(DB_DIR)

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts'] 

# Perform simple linear regression on y and elo_i
results = smf.ols('y~elo_n',data=nba).fit()
#print(results.summary())

# Create an analysis of variance table
aov_table = sm.stats.anova_lm(results, typ=2)

# Print the analysis of variance table
print(aov_table)


