#!/usr/bin/env python3

# Assignment: 1.15 LAB: Strip Plots
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/titanic.csv")

# load the titanic.csv dataset
titanic = pd.read_csv(DB_DIR)

# subset titanic to include male passengers in first class over 18 years old
df = titanic[(titanic['age'] > 18) & (titanic['sex'] == 'male') & (titanic['pclass'] == 1)]

print(df.head())

# plot
sns.swarmplot(x="embark_town", y="age", hue = "alive", data=df)

# saves the image
plt.savefig("titanicswarmplot.png")

# shows the image
plt.show()

