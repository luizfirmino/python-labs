#!/usr/bin/env python3

# Assignment 2 - Sort List
# Author: Luiz Firmino

# Scope
# Q1. To sort a list in descending order, call list method sort with the optional keyword argument ____ set to True.
# Q2. Insert 10 random letters in the range ‘a’ through ‘z’ into a list. Perform the following tasks and display your results
#   a. Sort the list in ascending order
#   b. Sort the list in descending order
#   c. Get the unique values sort them in ascending order

def getUniques(list):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
            
    return unique_list


print("Q1. To sort a list in descending order, call list method sort with the optional keyword argument **reverse** set to True.")
print()

letters = ['e', 'h', 'f', 'h', 'j', 'b', 'j', 'b', 'a', 'c']
print("Random Letters")
print(letters)
print()

print("Sort the list in ascending order.")
letters.sort()
print(letters)
print()

print("Sort the list in descending order.")
letters.sort(reverse = True)
print(letters)
print()

print("Unique values sorted in as ascending order.")
letters = getUniques(letters)
letters.sort()
print(letters)
print()
