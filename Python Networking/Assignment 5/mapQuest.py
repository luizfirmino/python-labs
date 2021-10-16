#!/usr/bin/env python3

# Assignment: 5 - MaqQuest REST API
# Author: Luiz Firmino
# DELIVERABLE 5_1: REWRITE THE ABOVE MAPQUEST API CALL TO INCLUDE GETTING USER INPUT FOR THE
# SOURCE AND DESTINATION POINTS. INCLUDE YOUR SCRIPT AND OUTPUT

import urllib.parse
import requests
import json
import webbrowser
from enum import Enum
import os
from os import path

CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
CONST_MQ_API_KEY_FILE = 'api_key_mq.txt'
CONST_MQ_API_END_POINT = 'https://www.mapquestapi.com/directions/v2/route?'

def get_api_key(FILENAME):
    '''this function reads a text file with the api Mapquest
    the key is returned as text '''

    with open(os.path.join(CONST_WORKING_DIR, FILENAME)) as api_key_fp:
        return (api_key_fp.readline())


def main():

    API_KEY = get_api_key(CONST_MQ_API_KEY_FILE)

    class routeTypeOptions(Enum):
        fastest = 1
        shortest = 2
        pedestrian = 3
        bicycle = 4
    
    routeOrig = input('Enter the origin: ')
    routeDest = input('Enter the destination: ')
    routeType = int(input('Enter the route type (1: fastest, 2: shortest, 3:pedestrian, 4:bicycle): '))
    routeUnit = input('Enter the unit (m: miles, k: kilometers): ')

    URL = CONST_MQ_API_END_POINT + urllib.parse.urlencode(
        {
            'key': API_KEY,
            'from': routeOrig,
            'to': routeDest,
            'routeType': routeTypeOptions(routeType).name,
            'unit': routeUnit
        }
    )

    json_data = requests.get(URL).json()
    response = requests.get(URL)
    
    if response.status_code == 200:
        print('*'*40)
        print(routeOrig, routeDest, sep='====>')
        print('Is this a toll road?',json_data['route']['hasTollRoad'])
        print('Distance:\t',json_data['route']['distance'])
        print('*'*40)
        print('Orig Long:\t',json_data['route']['boundingBox']['lr']['lng'])
        print('Orig Lat:\t',json_data['route']['boundingBox']['lr']['lat'])
        print('Dest Long:\t',json_data['route']['boundingBox']['ul']['lng'])
        print('Dest Lat:\t',json_data['route']['boundingBox']['ul']['lat'])
        print('*'*40)
    else:
        print('There was an error trying to process your request, please try again')

if __name__ == "__main__":
    main()