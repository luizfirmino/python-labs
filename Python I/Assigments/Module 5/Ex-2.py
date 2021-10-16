#
# Luiz Filho
# 3/14/2021
# Module 5 Assignment
# 2. In mathematics, the factorial of a number n is defined as n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n). 
# For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24. Write a recursive function for calculating n! 

def calculateN(num):
    if num == 1:
        return num
    else:
        return num * calculateN(num-1)
    
print(calculateN(4))
