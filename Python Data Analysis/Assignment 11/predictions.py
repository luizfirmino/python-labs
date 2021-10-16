#!/usr/bin/env python3

# Assignment: 3.12 LAB: Making predictions using SLR models
# Author: Luiz Firmino

import os
from os import path
import numpy as np
import pandas as pd
import statsmodels.formula.api as sms

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/internetusage.csv")

# load the file internetusage.csv
internet = pd.read_csv(DB_DIR)

model = sms.ols('internet_usage ~ bachelors_degree', data=internet).fit()

bach_percent = float(input())

# use the model.predict function to find the predicted value for internet_usage using 
# the bach_percent value for the predictor
prediction = internet[np.array([[bach_percent]]), internet['internet_usage']]
model.predict(prediction)
