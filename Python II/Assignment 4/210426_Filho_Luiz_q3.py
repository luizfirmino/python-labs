#!/usr/bin/env python3

# Assignment 4 - Q3
# Author: Luiz Firmino

# Scope
# Write a code segment that prints the names of all the items in the current working directory.

import os
from os import path

#CONST
CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))




#open current folder
for file1 in os.scandir(CONST_WORKING_DIR):
    if file1.is_file():
        print(file1.name)







