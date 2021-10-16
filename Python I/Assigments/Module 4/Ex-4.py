#
# Luiz Filho
# 3/7/2021
# Module 4 Assignment
# 4. The third equation of motion gives the final velocity of an object under
#    uniform acceleration given the distance traveled and an initial velocity:
# 
#   a. Using the equation above, build a function called (velocityFinal) which returns the final velocity of the object rounded to one decimal place. Use the following parameters
#
#        u or vo (initial velocity) 
#        a (uniform acceleration) 
#        d (distance traveled)

from math import sqrt

def velocityFinal(vo, a, d):
    return round((sqrt(sqrt(vo) + (2 * a * d))),1)


# b. As shown in the video above , a ball is gently dropped from a height of 51m (167 ft), 
# the acceleration due to gravity is a constant 9.8 m/s2. 
# Using the arguments described and function you built above, 
# what is the calling expression to determine the final velocity before impact?

print(velocityFinal(0, 9.8, 51)) 




def display_info(fname, lname, score):
    print("Hello, " , fname, " " , Lname)
    print("Your score on this exam is ", score)
    score = score + 5

def main():
    first = input("first name: ")
    last = input("last name: ")
    grade = input("exam score: ")
    display_info(last, first, score)

#if started as the main module, call the main function
 main()