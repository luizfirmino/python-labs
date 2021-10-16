#!/usr/bin/env python3

# Assignment 4 - Q4
# Author: Luiz Firmino

# Scope
# Write a code segment that prompts the user for a file. If the file does not 
# exist then the program should print an error. Otherwise, the program should print its contents.

import os
from os import path

def getFile():
    
    filePath = input('Enter the file path: ')

    #file1 = os.path.abspath(filePath)
    
    if path.exists(filePath):
        f = open(filePath, "r")
        print(f.read())
        f.close()
    else:
        print("FIle or path does not exist\n")

def main():

    continue_flag = True

    while continue_flag:

        getFile()

        continue_flag = (input('Continue? (y/n): ').lower() == 'y')
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()




