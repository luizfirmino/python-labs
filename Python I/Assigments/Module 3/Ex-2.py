#
# Luiz Filho
# 2/26/2021
# Module 3 Assignment
# 2. What is the output of the code below? Could you explain what happened ?
#

print("The code below demonstrate how the pass statement works")
print("When the condition i == 'mn' is true the pass statement simply keeps the program executing to the next instruction")
print("PS: in this example the condition i == 'mn' will never be true")

letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end="")