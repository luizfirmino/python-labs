#
# Luiz Filho
# 3/23/2021
# Module 6 Assignment
# 6. Write a program that takes your full name as input and displays the 
# abbreviations of the middle name except the first and last name which 
# is displayed as it is. 
# For example, if your name is Elvis Aaron Presley, then the output should be Elvis A. Presley.

fullName = input("Enter your full name ? ")

fullName = fullName.split(' ')

if len(fullName) <=2:
    print("You do not have middle name")
else:
    print("Your name is " + fullName[0] + " " + fullName[1][0].upper() + ". " + fullName[2])
