#
# Luiz Filho
# 3/14/2021
# Module 5 Assignment
# 3. . Write a recursive Python function that returns the sum of the first n integers. 
# (Hint: The function will be similar to the factorial function!) ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

def calculateSum(num):
    if num <= 1:
        return num
    else:
        return num + calculateSum(num-1)
    
print(calculateSum(3))
