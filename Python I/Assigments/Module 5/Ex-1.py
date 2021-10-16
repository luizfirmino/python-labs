#
# Luiz Filho
# 3/14/2021
# Module 5 Assignment
# 1. What is the Base Case in Recursion?

print("A base case in recursion is the first return without making any recursive execution, it's the condition that makes the recursion stops")
print("The base case used in the function below is 'num1 <= 10'")

def sumTwoNumbers(num1):
    if num1 <= 10:
        print(num1)
        return sumTwoNumbers(num1+1)
    
sumTwoNumbers(0)
