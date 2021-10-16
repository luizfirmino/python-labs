#
# Luiz Filho
# 3/14/2021
# Module 5 Assignment
# 4. Explain what happens when the following recursive functions is called with the value “alucard” and 0 as arguments:
# 

print("This recursive function is invalid, the function won't execute due an extra ')' character at line 12 column 29")
print("Regardless any value on its parameters this function will not execute or compile.")

def semordnilap(aString,index):
    if index < len(aString):
        print(aString[index]), end="")
        semordnilap(aString, index+1)

semordnilap("alucard", 0)