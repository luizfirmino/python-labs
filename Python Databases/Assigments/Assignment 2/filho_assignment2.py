#!/usr/bin/env python3

# Assignment 2 - Databases and Tables
# Author: Luiz Firmino

import sqlite3
import logging
import os
from os import path
import textwrap

logging.basicConfig(level=logging.DEBUG,format = "[Movies] : %(asctime)s : %(levelname)s : %(message)s") 
mypath = os.path.abspath(__file__)
DB_DIR = os.path.join(os.path.dirname(mypath), "movies.db")


def db_checkfile(dbfile):
   if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
      logging.debug("{a} found and not zero size".format(a=dbfile))
   else:
      logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   logging.debug("DB Connected".format())
   return con


def main():

    db_checkfile(DB_DIR)
    con = db_connect(DB_DIR)

    cur = con.cursor()
    #query to select all the elements from the movie table
    query = '''SELECT info_1.show_id , info_1.genre, info_1.title, info_1.director, info_2.release_year, info_2.description FROM movies_info_1 info_1 INNER JOIN movies_info_2 info_2 ON info_1.show_id = info_2.show_id'''

    #run the query
    cur.execute(query)

    #save the results in movies
    movies = cur.fetchall()

    print("List of Movies: \n")

    #loop through and print all the movies
    for movie in movies:
        logging.debug("{:5} {:30} {:20} {:20} {:>10} {:10}".format(movie[0] , movie[1] , movie[2] , movie[3] , movie[4] , movie[5]))
        
    print("\nDone - See you next time! \n")

    if con:
        con.close()


if __name__ == "__main__":
    main()