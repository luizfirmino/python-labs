#
# Luiz Filho
# 2/26/2021
# Module 3 Assignment
# 3. You are trying to build a program that will ask the user the following:
#       First Name
#       Temperature
# Based on the user's entries, the program will recommend the user to wear a T-shirt  
# if the temperature is over or equal to 70º or bring a sweater if it is less than 70º.
#

print("What shall I wear today?")
firstName = input("Please Enter Your First Name: ")
temperature = int (input("What is Today's Temperature: "))

if temperature >= 70:
    print("Hi " + firstName + " , It will be a warm day , T-shirt time!")
else:
    print("Hi " + firstName + ", You should probably bring a sweater")