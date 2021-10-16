#!/usr/bin/env python3

# Assignment 3 - SQL statements
# Author: Luiz Firmino

import sqlite3
import logging
import os
from os import path
import textwrap

logging.basicConfig(level=logging.DEBUG,format = "[Movies] : %(asctime)s : %(levelname)s : %(message)s") 
CONST_CURRENT_DIR = os.path.abspath(__file__)
CONST_DB_DIR = os.path.join(os.path.dirname(CONST_CURRENT_DIR), "filho_assignment3.db")

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   logging.debug("DB Connected".format())
   return con

def execSQL(conn, sql):
   conn.execute(sql)
   logging.debug("SQL Statement executed".format())


def main():

   con = db_connect(CONST_DB_DIR)
   
   # TABLE: movies_info_1
   execSQL(con, '''CREATE TABLE IF NOT EXISTS [movies_info_1] ([show_id] INTEGER, [genre] TEXT, [title] TEXT, [director] TEXT, PRIMARY KEY([show_id] AUTOINCREMENT));''')
   
   # TABLE: movies_info_2
   execSQL(con, '''CREATE TABLE IF NOT EXISTS [movies_info_2] ([show_id]	INTEGER, [release_year]	INTEGER, [description]	TEXT, FOREIGN KEY([show_id]) REFERENCES [movies_info_1]([show_id]), PRIMARY KEY([show_id]));''')
       
   # First movie
   execSQL(con, '''INSERT INTO [movies_info_1] ([genre], [title], [director]) VALUES('Animation', 'Toy Story', 'Stanton');''')
   execSQL(con, '''INSERT INTO [movies_info_2] VALUES(last_insert_rowid(), 1995, 'Stars come to life as they work to be reunited with Andy');''')

   # Second movie
   execSQL(con, '''INSERT INTO [movies_info_1] ([genre], [title], [director]) VALUES('Animation', 'Finding Nemo', 'Stanton');''')
   execSQL(con, '''INSERT INTO [movies_info_2] VALUES(last_insert_rowid(), 2003, 'Adventures of Nemo and his friend, Dory');''')

   # Third movie
   execSQL(con, '''INSERT INTO [movies_info_1] ([genre], [title], [director]) VALUES('Animation', 'Cars', 'Lasseter');''')
   execSQL(con, '''INSERT INTO [movies_info_2] VALUES(last_insert_rowid(), 2006, 'Story of a car lost in Radiator Springs');''')

   con.commit()
   logging.debug("DB changes committed!".format())
   
   print()
   print("My Movie Database\n")

   # Query to select all the elements from the movie table
   cur = con.cursor()
   cur.execute('''SELECT info_1.genre, info_1.title, info_1.director, info_2.release_year, info_2.description FROM movies_info_1 info_1 INNER JOIN movies_info_2 info_2 ON info_1.show_id = info_2.show_id''')

   # Save the results in the cursor
   movies = cur.fetchall()

   # Table HEADERS
   print("{:20} {:20} {:20} {:>10} {:10}".format("Genre", "Title", "Director", "Year", "Description"))

   # loop through and print all the movies
   for movie in movies:
      print("{:20} {:20} {:20} {:>10} {:10}".format(movie[0] , movie[1] , movie[2] , movie[3] , movie[4]))

   # Conclude the execution
   print("\nDone - See you next time!\n")

   if con:
      con.close()
      logging.debug("DB connection closed".format())


if __name__ == "__main__":
    main()