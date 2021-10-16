#!/usr/bin/env python3

# Assignment 1 - Birthday Calculator
# Author: Luiz Firmino

# Scope
# 2. Create a program that accepts a name and a birth date and displays the person’s birthday,the current day, the person’s age, and the number of days until the person’s next birthday.
# Allow the user to enter a date in the MM/DD/YY format. Adjust the date so that it is correct even if the birth year is later than the current year.
# When you calculate the person’s age, don’t take leap year into account. If the person is more than 2 years old, display the person’s age in years. Otherwise, display the person’s age in days.
# When you display the message that indicates the number of days to the person’s birthday, you can use the following format for a person with a name of John: 
# today - John's birthday is today!
# tomorrow - John's birthday is tomorrow!
# yesterday - John's birthday was yesterday!
# other days - John's birthday is in X days

from datetime import datetime, timedelta

def getName():

    while True:
        value = input('Enter name: ')

        if value != '':
            return value
        else:
            print("Incorrect data format\n")
            continue


def getBirthday():

    while True:
        value = input('Enter birthday (MM/DD/YY): ')

        try:
            value = datetime.strptime(value, '%m/%d/%Y')
            return value
            
        except ValueError:
            print("Incorrect data format\n")
            continue

def main():

    continue_flag = True

    print('Birthday Calculator \n')  

    while continue_flag:

        # Enter values
        name = getName()
        birthday = getBirthday()

        # Calculate Birthday
        today = datetime(datetime.now().year, datetime.now().month, datetime.now().day) # it formats the date without time
        next_birthday = datetime(datetime.now().year, birthday.month, birthday.day)
        days_to_next_birthday = (next_birthday - today).days
        days = ((today - birthday).days / 365 / 4) # it solves the gap between leap years
        years_old = int(((today - timedelta(days=days) - birthday).days / 365))

        print("Birthday:", birthday.strftime('%A, %B %d, %Y'))
        print("Today:", datetime.now().strftime('%A, %B %d, %Y'))
        print(name, "is", years_old, "years old")
        
        if days_to_next_birthday == 0:
            print(name,"'s birthday is Today!")
        elif days_to_next_birthday == 1:
            print(name,"'s birthday is Tomorrow!")
        elif days_to_next_birthday == -1:
            print(name,"'s birthday was Yesterday!")
        else:
            print(name,"'s birthday is in", days_to_next_birthday, "days.")
              
        continue_flag = (input('Continue? (y/n): ').lower() == 'y')
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()