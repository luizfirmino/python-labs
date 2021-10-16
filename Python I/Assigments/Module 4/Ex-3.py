#
# Luiz Filho
# 3/7/2021
# Module 4 Assignment
# 3. What will the following Python program print out? Explain the output

print("The functions below well defined to print pre-determined strings. Each function was built to output parts of a whole sentence that could be completed by executing the function in the correct order. Not the way they were organized and listed in the code.")
print("Important note: the second parameter of the function print were used to make sure the string do not break a new line.")
print("")

def name():
    print("- Albert Einstein")
def quote():
    print("Imagination is more important than ", end="")
def ofthe():
    print("For knowledge is limited, ", end="")
def day():
    print("knowledge. " , end="")
def famous():
    print("stimulating progress, giving birth to evolution ", end="")
def influencers():
    print("whereas imagination embraces the entire world, ", end="")

quote()
day()
ofthe()
influencers()
famous()
name()