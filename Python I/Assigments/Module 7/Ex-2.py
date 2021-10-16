#
# Luiz Filho
# 4/7/2021
# Module 7 Assignment
# 2. The data type integer signed range is from -2,147,483,648 to 2,147,483,647 (4 bytes). 
# Write a program that determines the range of numbers for an integer based on the number 
# of bytes it can encode (Hint integral type with n bits can encode 2n numbers). 


number = int(input("Enter number of Bytes you would like to determine the signed range of: "))

bits = (number * 2)
size = (2 ** (bits*number))

print(str(number) + " Byte(s) integral type with " + str(bits) + " bits can encode " + str(size) + " numbers. The signed range will be from -2,147,483,648 to 2,147,483,647")
