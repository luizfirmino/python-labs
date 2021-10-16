#
# Luiz Filho
# 4/7/2021
# Module 7 Assignment
# 1. Write a program to print and insert the value of tau 
# in an available field width space of 8 characters (center aligned) 
# , also print and insert the value of ½ tau to determine the value 
# and insert / center align as shown in the first console 
# example below). Not too sure what Tau is (or its associated numerical value) ?  

# Import math Library
import math
print("The value of Tau is " + "[{:^8.2f}]".format(math.tau) + ", which is two times " + "[{:^8.2f}]".format((math.tau/2)) + ".")
