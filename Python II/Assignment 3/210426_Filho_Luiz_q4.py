#!/usr/bin/env python3

# Assignment 3 - Q4
# Author: Luiz Firmino

# Scope
# Which of the following are immutable data structures? Why ? Please explain
#   dictionaries and lists
#   strings and tuples


print("Which of the following are immutable data structures?")
print()
print("a. dictionaries and lists are Mutable")
print("Mutable data types in Python allows you to change its value")
print()

list1 = [1, 2, 3]
print("list1 = [1, 2, 3]")

dic1 = {"full_name" : ["Luiz", ""]}
print("dic1 = {'full_name' : ['Luiz', '']}")
print()

list1[1] = "3500"
print("list1[1] = 3500")

dic1["full_name"][1] = "Firmino"
print("dic1['full_name'][1] = Firmino")
print()

print("Result:")
print("list1[1] = ", list1[1])
print("dic1['full_name'][1]", dic1["full_name"][1])
print()

print("b. strings and tuples are inmutable")
print("Inmutable data types in Python does not allow you to change its value once it's defined")

tuple1 = (1, 2, 3)
print("turple1 = (1, 2, 3)")

str1 = "Luiz"
print("str1 = 'Luiz' id = ", id(str1))
print()

print("tuple1[1] = '3500'")
try:
    tuple1[1] = "3500"
except TypeError:
    print("object does not support item assignment\n")

str1 = "Firmino"
print("str1 = 'Firmino' id = ", id(str1))
print()