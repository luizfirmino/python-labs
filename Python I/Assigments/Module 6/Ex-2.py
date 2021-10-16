#
# Luiz Filho
# 3/23/2021
# Module 6 Assignment
# 2. Take the following Python code that stores a string: 
# str = 'inet addr:127.0.0.1  Mask:255.0.0.0'. 
# Use find and string slicing to extract 
# the portion of the string after the colon inet address 
# character and then use the rstrip function 
# to remove any trailing characters.

str = 'inet addr:127.0.0.1  Mask:255.0.0.0' 
print(str[slice(str.find(":")+1,-1)].rstrip())
