#!/usr/bin/env python3

# Assignment: 1.14 LAB: Line Charts
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/target.csv")

# load the target.csv file
tgt = pd.read_csv(DB_DIR)

# subset the last 19 days of the dataframe
tgt_march = tgt[-19:]

# subset tgt_march and create a data frame that contains the columns: Date and Volume
tgt_vol = tgt_march[["Date","Volume"]]

# subset tgt_march and create a data frame that contains the columns: Date and Closing
tgt_close = tgt_march[["Date","Close"]]

day = int(input())

# subset the specific row of tgt_vol for the given day
volume_row = tgt_vol[pd.to_datetime(tgt_vol['Date']).dt.strftime('%d') == str(day)]
volume = volume_row.iloc[0][1] # gets the volume for the given day

# subset the specific row of tgt_close for the given day
close_row = tgt_close[pd.to_datetime(tgt_close['Date']).dt.strftime('%d') == str(day)]
close = close_row.iloc[0][1] # gets the closing stock price for the given day

date = tgt_march[pd.to_datetime(tgt_march['Date']).dt.strftime('%d') == str(day)].iloc[0][0] # gets the date

print("The volume of TGT on", date, "is", volume)
print("The closing stock price of TGT on", date, "is $", close)

# title
plt.title('March 2018 Trading Volume for Target Stock', fontsize = 20)

# x and y axis labels
plt.xlabel('Date')
plt.ylabel('Number of trades')

# plot
plt.plot(pd.to_datetime(tgt_march["Date"]).dt.strftime('%d'), tgt_march["Volume"])

# saves the image
plt.savefig("linechart.png")

# shows the image
plt.show()

# title
plt.title('March 2018 CLosing Volume for Target Stock', fontsize = 20)

# x and y axis labels
plt.xlabel('Date')
plt.ylabel('Price')

# plot
plt.plot(pd.to_datetime(tgt_march["Date"]).dt.strftime('%d'), tgt_march["Close"])

# saves the image
plt.savefig("linechart.png")

# shows the image
plt.show()