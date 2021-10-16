#!/usr/bin/env python3

# Assignment: 2 - Lists
# Author: Luiz Firmino

list = [1,2,4,'p','Hello']  #create a list
print(list)                 #print a list
list.append(999)            #add to end of list
print(list)
print(list[-1])             #print the last element
list.pop()                  #remove last element
print(list)
print(list[0])              #print first element
list.remove(1)              #remove element
print(list)
del list[3]                 #remove an element by index
print(list)
list.insert(0,'Baby')       #insert an element at index
print(list)