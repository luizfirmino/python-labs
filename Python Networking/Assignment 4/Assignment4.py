#!/usr/bin/env python3

# Assignment: 4 - Files
# Author: Luiz Firmino
# DELIVERABLE 4. SUBMIT A COPY OF YOUR SCRIPT TO WRITE YOUR JSON FILE AND THE OUTPUT FOR READING YOUR JSON FILE.

import json
import os
from os import path
from faker import Faker

CONST_WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
CONST_JSON_SOURCE = 'my_file.json'
CONST_WRIGHT_MODE = 'w'
CONST_READ_MODE = 'r'

# create a Json File
def createJsonFile(file_name, data):
    
    # write the json file
    with open(file_name, CONST_WRIGHT_MODE) as json_file:
        json.dump(data, json_file)
        print(file_name, 'generated')


def readJsonFile(file_name):
    with open(file_name, CONST_READ_MODE) as json_file:
        data = json.load(json_file)
        for node in data:
            print('JSON DATA: ', data[node])


def main():

    json_file = os.path.join(CONST_WORKING_DIR, CONST_JSON_SOURCE);

    fake = Faker()
    json_data = {}
    json_data['person'] = []

    for _ in range(10):
        json_data['person'].append({'name': fake.name(), 'address':fake.address()})

    createJsonFile(json_file, json_data)
    readJsonFile(json_file)


if __name__ == "__main__":
    main()