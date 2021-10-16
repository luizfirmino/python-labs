#
# Luiz Filho
# 2/16/2021
# Module 2 Assignment
# 3. Write a program which prompts the user to enter the mass in pounds, converts the mass to kg, and prints: 
# a. The converted mass in kgs (1 kg = 2.20462 lbs) 
# b. The weight of the mass on Earth (Newtons)  = mass (kg) x 9.807 (m/s^2)
# c. The weight of the mass on the Moon (Newtons)  = mass (kg) x 1.62 (m/s^2)
# d. The percentage of the weight on the Moon in comparison to what is experienced on Earth = Weight on Moon / Weight on Earth x 100
# e. The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer

import math

mass_lbs = input("Please enter the mass in lb that you would like to convert to kg: ")
mass_lbs = int(mass_lbs)

mass_kilos = (mass_lbs/2.20462)
print("The converted mass in kg is: " + str(mass_kilos))

weight_earth = (mass_kilos * 9.807)

print("Your weight on Earth is: " + str(weight_earth) + " Newtons")

weight_moon = (mass_kilos * 1.62)

print("Your weight on the Moon is: " + str(weight_moon) + " Newtons")
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth: " + str(((weight_moon/weight_earth) * 100)) + "%")
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is " + str(math.ceil(((weight_moon/weight_earth) * 100))) + "%")