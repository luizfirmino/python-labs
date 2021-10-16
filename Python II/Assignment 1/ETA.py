#!/usr/bin/env python3

# Assignment 1 - ETA Calculator
# Author: Luiz Firmino

# Scope
# 1. Create a program that calculates the estimated duration of a trip in hours and minutes (same time zone). 
# This should include an estimated date/time of departure and an estimated date/time of arrival:
# - For the date of departure and arrival, the program should use the YYYY-MM-DD format for dates
# - For the time of departure and arrival , the program should use the HH:MM AM/PM format for times.
# - For the miles and miles per hour, the program should only accept integer entries like 200 and 65.
# - Assume that the user will enter valid data.

from datetime import datetime, timedelta

def getDepartureDate():

    while True:
        value = input('Estimated date of departure (YYYY-MM-DD): ')

        try:
            value = datetime.strptime(value, '%Y-%m-%d')
            return value

        except ValueError:
            print("Incorrect data format\n")
            continue


def getDepartureTime():

    while True:
        value = input('Estimated time of departure (HH:MM AM/PM): ')

        try:
            value = datetime.strptime(value, '%I:%M %p')
            return value
            
        except ValueError:
            print("Incorrect data format\n")
            continue

def getMiles():

    while True:
        value = input('Enter miles: ')

        try:
            value = int(value)
            return value

        except ValueError:
            print("Incorrect data format\n")
            continue

def getMPG():

    while True:
        value = input('Enter miles per hour: ')

        try:
            value = int(value)
            return value

        except ValueError:
            print("Incorrect data format\n")
            continue

def main():

    continue_flag = True

    print('Arrival Time Estimator \n')
    
    while continue_flag:

        # Enter values
        departure_date = getDepartureDate()
        departure_time = getDepartureTime()
        miles = getMiles()
        mph = getMPG()

        # Calculate ETA
        hours = (int(miles) / int(mph))
        minutes = (( (int(miles) / int(mph)) - int(hours) ) * 60)
        departure_date_time = departure_date + timedelta(hours=departure_time.hour, minutes=departure_time.minute)
        date_arrival = departure_date_time + timedelta(hours=hours, minutes=minutes)

        print()
        print('Estimated travel time')
        print('Hours: ', hours)
        print('Minutes: ', minutes)
        print('Estimated date of arrival: ', date_arrival.strftime('%Y-%m-%d'))
        print('Estimated time of arrival: ', date_arrival.strftime('%I:%M %p'))

        continue_flag = (input('Continue? (y/n): ').lower() == 'y')

if __name__ == "__main__":
    main()