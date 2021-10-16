#!/usr/bin/env python3

# Assignment 1 - Artist List
# Author: Luiz Firmino

#imports at top of file
import sqlite3

def main():
    con = sqlite3.connect('chinook.db')

    cur = con.cursor()
    #query to select all the elements from the movie table
    query = '''SELECT * FROM artists'''

    #run the query
    cur.execute(query)

    #save the results in movies
    artists = cur.fetchall()

    print("List of Artists: \n")

    #loop through and print all the movies
    for artist in artists:
        print(artist[0] , " " , artist[1])

    print("\nDone - See you next time! \n")

    if con:
        con.close()

if __name__ == "__main__":
    main()