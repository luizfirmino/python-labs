#
# Luiz Filho
# 3/23/2021
# Module 6 Assignment
# 5. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#
#Console Output
#
#What is your first name ? alison
#What is your last name ? smith
#Hi Alison Smith , welcome to my Python greet application!

firstName = input("What is your first name ? ")
lastName = input("What is your last name ? ")

print("Hi " + firstName.replace(firstName[0], firstName[0].upper(), 1) + " " + lastName.replace(lastName[0], lastName[0].upper(), 1) + " , welcome to my Python greet application!")
