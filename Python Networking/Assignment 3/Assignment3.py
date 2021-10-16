#!/usr/bin/env python3

# Assignment: 3 - Lists
# Author: Luiz Firmino
# PROVIDE YOUR SCRIPT FOR
# POPULATING A LIST WITH RANDOM INTEGERS USING A FOR LOOP THEN USING LIST COMPREHENSION


# POPULATING A LIST WITH RANDOM INTEGERS USING A FOR LOOP
integers_list = []
for x in range(2, 30, 3):
  integers_list.append(x)
print('integers list:', integers_list)

# POPULATING A LIST WITH RANDOM INTEGERS USING LIST COMPREHENSION
comprehension_list = [x for x in integers_list]
print('comprehension list:', comprehension_list)