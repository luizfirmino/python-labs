#!/usr/bin/env python3

# Assignment 5 - Visualizing Data
# Author: Luiz Firmino

import sqlite3
import os
from os import path
import matplotlib.pyplot as plt
import numpy as np

CONST_CURRENT_DIR = os.path.abspath(__file__)
CONST_DB_DIR = os.path.join(os.path.dirname(CONST_CURRENT_DIR), "degrees2.db")

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   return con     


def main():

    con = db_connect(CONST_DB_DIR)
    cur = con.cursor()
    result = cur.execute("SELECT * FROM degrees ORDER BY YEAR")
    degrees = result.fetchall()

    # Graph DATA
    allyears, agriculture, biology, business, education = [], [], [], [], []

    for row in degrees:
        allyears.append(row[0])
        agriculture.append(row[1])
        biology.append(row[4])
        business.append(row[5])
        education.append(row[8])  
    
    # plot lines
    plt.plot(allyears, agriculture, label = "Agriculture")
    plt.plot(allyears, biology, label = "Biology")
    plt.plot(allyears, business, label = "Business")
    plt.plot(allyears, education, label = "Education")
    plt.ylabel('Degrees')    
    plt.xlabel('Year') 
    plt.title("% of Bachelor's degrees for USA women by major (1970-2011)\n\nDegrees Over Time")
    plt.legend()
    plt.show()   

    if con:
        con.close()

if __name__ == "__main__":
    main()