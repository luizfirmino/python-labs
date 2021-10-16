#
# Luiz Filho
# 4/7/2021
# Module 7 Assignment
# 3. Gases consist of atoms or molecules that move at different speeds in random directions. 
# The root mean square velocity (RMS velocity) is a way to find a single velocity value for the particles. 
# The average velocity of gas particles is found using the root mean square velocity formula:
#
# μrms = (3RT/M)½ root mean square velocity in m/sec
#
# R = ideal gas constant = 8.3145 (kg·m2/sec2)/K·mol
#
# T = absolute temperature in Kelvin
#
# M = mass of a mole of the gas in kilograms. molar mass of O2 = 3.2 x 10-2 kg/mol
#
# T = °C + 273
#
# a. By using the decimal module, create a decimal object and apply the sqrt and quantize method (match pattern “1.000”) 
# and provide the answer to the question:  
# What is the average velocity or root mean square velocity of a molecule in a sample of oxygen at 25 degrees Celsius?

number = 3237945.76

print("{:25,.9f}".format(number))

print("{:.2f}".format(number))

print("{:,.2f}".format(number))

print("{:,.4f}".format(number))

