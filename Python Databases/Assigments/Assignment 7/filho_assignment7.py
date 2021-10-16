#!/usr/bin/env python3

# Assignment 7 - Database Analysis
# Author: Luiz Firmino

import sqlite3
import os
from os import path
import matplotlib.pyplot as plt
import pandas as pd

CONST_CURRENT_DIR = os.path.abspath(__file__)
CONST_DB_DIR = os.path.join(os.path.dirname(CONST_CURRENT_DIR), "beers.db")

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   return con     

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

def main():

    #connect to sqlite database
    con = db_connect(CONST_DB_DIR)

    # Read sqlite query results into a pandas DataFrame
    df = pd.read_sql_query("SELECT * from reviews", con)

    print("------------------------------ QUESTION ------------------------------")
    print("Question 1: How many rows are in the table?")
    print("------------------------------  ANSWER  ------------------------------")
    print(str(len(df)), "rows")
    print("----------------------------------------------------------------------")
    print()

    print("------------------------------ QUESTION ------------------------------")
    print("Question 2: Describe the table")
    print("------------------------------  ANSWER  ------------------------------")
    print(df.describe())
    print("----------------------------------------------------------------------")
    print()
    
    print("------------------------------ QUESTION ------------------------------")
    print("Question 3: How many entries are there for each brewery")
    print("------------------------------  ANSWER  ------------------------------")
    print_full(df.groupby(['brewery_name']).size())
    print("----------------------------------------------------------------------")
    print()
    
    print("------------------------------ QUESTION ------------------------------")
    print("Question 4: Find all entries are low alcohol.  Alcohol by volume (ABV) less than 1%")
    print("------------------------------  ANSWER  ------------------------------")
    low_abv = df[df.beer_abv < 1]
    print_full(low_abv)
    print("----------------------------------------------------------------------")
    print()
    
    print("------------------------------ QUESTION ------------------------------")
    print("Question 5:How many reviews are there for low ABV beers?")
    print("------------------------------  ANSWER  ------------------------------")
    print(len(low_abv),"reviews")
    print("----------------------------------------------------------------------")
    print()
    
    print("------------------------------ QUESTION ------------------------------")
    print("Question 6:Group the AVB beers by beer and count")
    print("------------------------------  ANSWER  ------------------------------")
    grouping = low_abv.groupby('beer_name')
    print_full(grouping.size())
    print("----------------------------------------------------------------------")
    print()
    
    print("Question 7:How consistent are the O'Douls overall scores?")
    odouls = low_abv[low_abv.beer_name == "O'Doul's"]['review_overall']
    print("------------------------------  ANSWER  ------------------------------")
    print_full(odouls)
    print("----------------------------------------------------------------------")
    print()

    print("------------------------------ QUESTION ------------------------------")
    print("Question 8:Plot a histogram of O'Douls overall scores (may need to close window to continue)")
    odouls.hist()
    plt.show()
    print("Graph generated")
    print("----------------------------------------------------------------------")
    print()

    print("------------------------------ QUESTION ------------------------------")
    print("Question 9:For O'Douls, what are the mean and standard deviation for the O'Doul's overall scores?")
    print("------------------------------  ANSWER  ------------------------------")
    print("mean =",odouls.mean())
    print("deviation =",odouls.std())
    print("----------------------------------------------------------------------")
    print()

    print("------------------------------ QUESTION ------------------------------")
    print("Question 10:Draw a boxplot of the low_abv data (may need to close window to continue)")
    print("------------------------------  ANSWER  ------------------------------")
    low_abv.boxplot(figsize=(12,10))
    plt.show()
    print("Graph generated")
    print("----------------------------------------------------------------------")
    print()

    if con:
        con.close()

if __name__ == "__main__":
    main()