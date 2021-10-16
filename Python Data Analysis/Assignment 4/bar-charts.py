#!/usr/bin/env python3

# Assignment: 1.12 LAB: Subsetting data frames
# Author: Luiz Firmino

import os
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "../csvfiles/titanic.csv")

# load the pandas module as pd
titanic = pd.read_csv(DB_DIR)

# subset the titanic dataset to include first class passengers who embarked in Southampton
first_south = titanic[(titanic['pclass'] == 1) & (titanic['embarked'] == 'S')]

# subset the titanic dataset to include either second or third class passengers
second_third = titanic[titanic['pclass'].isin([2,3])]

print(first_south.head())
print(second_third.head())

# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True)

# title
plt.title('Passenger Class', fontsize=20)

# plots a vertical bar chart
sns.countplot(x="class", color="b", data=titanic);

# saves the image
plt.savefig("verticalbarchart.png")

# shows the image
plt.show()


# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True)

# title
plt.title('Passenger Class', fontsize=20)

# generates a vertical bar chart
sns.countplot(x="class", hue="survived", color="g", data=titanic);

# saves the image
plt.savefig("groupedbarchart.png")

# shows the image
plt.show()

