#!/usr/bin/env python3

# Assignment 4 - Q1
# Author: Luiz Firmino

# Scope
# Write a code segment that opens a file named file.txt for input and prints the number of lines in that file.

import os
from os import path

#CONST
CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

#open file
f = open(os.path.join(CONST_WORKING_DIR, "file.txt"), "r")
#counter
lines = 0

#split file by pagebreak
file1 = f.read().split("\n")
for i in file1:
    if i:
        lines += 1
          
print("The files contains", lines, "lines!")

#close the file
f.close()