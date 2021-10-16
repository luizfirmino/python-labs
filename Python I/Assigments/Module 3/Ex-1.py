#
# Luiz Filho
# 2/26/2021
# Module 3 Assignment
# 1. What is the difference between “pass” and “continue” in Python?
#

print("The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. See example below.")

a = [0, 1, 2, 3]
for i in a:
     if i == 2:
         pass
     print(i)

print()
print("The continue statement skips the next instruction and returns the execution to its caller. See example below")

for i in a:
     if i == 2:
         continue
     print (i)



     print(print.__doc__)