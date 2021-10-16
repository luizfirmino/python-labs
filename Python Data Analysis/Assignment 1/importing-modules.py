#!/usr/bin/env python3

# Assignment: 1.10 LAB: Importing modules
# Author: Luiz Firmino

import numpy as np
import scipy.stats as st

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

x = np.array([x1, x2, x3, x4])
y = np.array([0, 10, 7, 25])

print(st.linregress(x,y))
