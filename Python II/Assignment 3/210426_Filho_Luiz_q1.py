#!/usr/bin/env python3

# Assignment 3 - Q1
# Author: Luiz Firmino

# Scope
# What does this code do?
# The dictionary temperatures contain four Fahrenheit samples for each of five days. What does the “for” statement do?

temperatures = {
'Monday': [67, 71, 74, 77],
'Tuesday': [52, 56, 66 , 50],
'Wednesday': [77, 80, 87 , 95],
'Thursday': [67, 77, 81 , 77],
'Friday': [54 , 60 , 67, 60],
}
for k, v in temperatures.items():
     print(f'{k}: {sum(v)/len(v):.0f}')

print("The for statement goes through the dictionary and calculates the average of the values presented in the array")