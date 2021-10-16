#!/usr/bin/env python3

# Assignment 4 - more SQL
# Author: Luiz Firmino

import sqlite3
import logging
import os
from os import path
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,format = "[Movies] : %(asctime)s : %(levelname)s : %(message)s")
CONST_CURRENT_DIR = os.path.abspath(__file__)
CONST_DB_DIR = os.path.join(os.path.dirname(CONST_CURRENT_DIR), "dbmovies.sqlite")

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   logging.debug("DB Connected".format())
   return con


def execSQL(conn, sql):

    try:
        conn.execute(sql)
        logging.debug("SQL Statement executed".format())
    except:
        logging.debug("SQL Statement exception error attempting to update the database".format())
        conn.close()
        quit()
        

def getYear():

    while True:
        value = input('Please enter the year to lookup: ')

        try:
            int(value)
            return value

        except ValueError:
            print("Incorrect data format\n")
            continue


def main():

    con = db_connect(CONST_DB_DIR)
    
    # Database updates:
    # Using python and SQL, in the Movie table update the year in Toy Story, it should be 1995.
    execSQL(con, "UPDATE Movie SET year = '1995' WHERE name LIKE 'Toy Story%';")
    
    # We lost our only copy of  Lawrence of Arabia, using python and SQL delete that movie from the database
    execSQL(con, "DELETE FROM movie WHERE name LIKE '%Lawrence of Arabia%';")
    
    con.commit()

    print("Welcome to the MovieDB!\n")

    while True:

        year = getYear()
        
        cur = con.cursor()
        result = cur.execute("SELECT m.name as title, m.year, m.minutes as length, c.name as genre FROM Movie m INNER JOIN Category c ON m.categoryID = c.categoryID WHERE m.year = ?", [year])
        
        movies = result.fetchall()
        
        if (len(movies) > 0):

            print() # Spacer

            # HEADERS
            print("{:40} {:>10} {:>10} {:20}".format("TITLE", "YEAR", "LENGTH", "GENRE"))

            # loop through and print all the results
            for movie in movies:
                print("{:40} {:>10} {:>10} {:20}".format(movie[0] , movie[1] , movie[2] , movie[3]))

        else:
            print("Sorry, no movie in our database for", year)
        

        print()
        if (input('Look up another year (y/n)? ').lower() == 'n'):
            break


    # Conclude the execution
    print("\nBye for now - see you at the movies!\n")

    if con:
        con.close()
        logging.debug("DB connection closed".format())


if __name__ == "__main__":
    main()