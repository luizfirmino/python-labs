#!/usr/bin/env python3

# Assignment 4 - Q2
# Author: Luiz Firmino

# Scope
# Write a code segment that opens a file for input and prints the number of five-letter words in the file.

import os
from os import path

#CONST
CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

#open file
f = open(os.path.join(CONST_WORKING_DIR, "file.txt"), "r")

#counter
count_5_letter_words = 0

#list
words = []

#split file by pagebreak
file1 = f.read().split("\n")
for line in file1:
    for word in line.split(" "):
        if len(word) == 5:
            words.append(word)
            count_5_letter_words += 1

print("There are", count_5_letter_words, "words with 5 letters in the file")
print(words)
print()

#close the file
f.close()






