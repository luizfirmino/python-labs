#!/usr/bin/env python3

# Assignment 3 - Q2
# Author: Luiz Firmino

# Scope
# Following the instructions, write a script that counts duplicate words.
# Techniques like word frequency counting are often used to analyze published work. Other document analysis techniques are in natural language processing. Write a script that uses a dictionary to determine and print the number of duplicate words in a sentence. Treat uppercase and lowercase letters the same and assume there is no punctuation in the sentence. Words with counts larger than one have duplicates.

phrase = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked"

wordsCount = {}

for word in phrase.rsplit(" "):
    if word in wordsCount:
        wordsCount[word] = wordsCount[word] + 1
    else:
        wordsCount[word] = 1

print("{:<10}{:^5}".format("WORD" , "COUNT"))
for k, v in wordsCount.items():
     print("{:<10}{:^5}".format(k , v))