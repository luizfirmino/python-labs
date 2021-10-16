#
# Luiz Filho
# 2/16/2021
# Module 2 Assignment
# Assume that we execute the following assignment statements
# 
# length = 10.0 , width = 7
# 
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 
#     width//2
#     length/2.0
#     length/2
#     1 + 4 * 5
#

length = 10.0
width = 7

print("-- DEFAULTS --------------")
print("Variable width value = " + str(width))
print("Variable length value = " + str(length))
print("--------------------------")

print("Result of width//2: " + str(width//2) + " output type:" + str(type(width//2)))
print("Result of length/2.0: " + str(length/2.0) + " output type:" + str(type(length/2.0)))
print("Result of length/2: " + str(length/2) + " output type:" + str(type(length/2)))
print("Result of 1 + 4 * 5: " + str((1 + 4 * 5)) + " output type:" + str(type((1 + 4 * 5))))
