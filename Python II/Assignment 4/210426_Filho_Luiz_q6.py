#!/usr/bin/env python3

# Assignment 4 - Q6
# Author: Luiz Firmino

# Scope
#  In the accounts.txt file:
# update the name 'Zoltar' to 'Robert' 
# create a tempfile with the new data
# remove accounts.txt file from the directory
# rename the tempfile to a new file called myaccounts.txt

import os
from os import path

# CONST
CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

CONST_ACCOUNTS_FILE = "accounts.txt"
CONST_TEMP_FILE ="_temp.txt"

def renameFile(filePath, newName):
    if path.exists(filePath):
        os.rename(filePath, newName)
    else:
        print("Cannot rename it! File or path does not exist\n")

def deleteFile(filePath):    
    if path.exists(filePath):
        os.remove(filePath)
    else:
        print("Cannot delete! File or path does not exist\n")


def main():

    # check if accounts file exists
    if path.exists(os.path.join(CONST_WORKING_DIR, CONST_ACCOUNTS_FILE)):
        
        print(CONST_ACCOUNTS_FILE, "exists")

        # open Accounts.txt file
        f = open(os.path.join(CONST_WORKING_DIR, CONST_ACCOUNTS_FILE), "r")
        print(CONST_ACCOUNTS_FILE, "opened")

        # open temp file
        f_temp = open(os.path.join(CONST_WORKING_DIR, CONST_TEMP_FILE), "w")
        print(CONST_TEMP_FILE, "created")

        file1 = f.read().split("\n")
        for line in file1:
            if "Zoltar" in line:
                data = line.replace('Zoltar', 'Robert')
                print(line, " replaced by ", data)
                f_temp.write(data  + '\n')
                print(data, " written in", CONST_TEMP_FILE)
            else:
                f_temp.write(line  + '\n')
                print(line, " written in", CONST_TEMP_FILE)

        # close files
        f.close()
        print(CONST_ACCOUNTS_FILE, "closed")
        f_temp.close()
        print(CONST_TEMP_FILE, "closed")

        # delete file Accounts.txt
        deleteFile(os.path.join(CONST_WORKING_DIR, CONST_ACCOUNTS_FILE))
        print(CONST_ACCOUNTS_FILE, "deleted")

        # rename temp file
        renameFile(os.path.join(CONST_WORKING_DIR, CONST_TEMP_FILE), "myaccounts.txt")
        print(CONST_TEMP_FILE, "rename to", "myaccounts.txt")


    else:
        print("File", CONST_ACCOUNTS_FILE, "does not exist!")

    

if __name__ == "__main__":
    main()




