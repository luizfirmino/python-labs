#!/usr/bin/env python3

# Assignment: 2.8 LAB: Five number summary
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/internetusage.csv")

df = pd.read_csv(DB_DIR)

population = df[["State","Population"]]

state_index = str(input('Enter the State name: '))

state_data = population[population['State'] == state_index]
print(state_data)

state_name = state_data.iloc[0][0]

state_pop = state_data.iloc[0][1]

print("The population of " + str(state_name) + " is " + str(state_pop)+ ".")

sns.set_style('whitegrid')

ax = sns.boxplot(y='Population', data=population)
ax = sns.stripplot(y="Population", data=population)

# saves the image
plt.savefig("titanicswarmplot.png")

# shows the image
plt.show()
