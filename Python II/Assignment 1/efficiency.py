#!/usr/bin/env python3

# Assignment 1 - Time Cost
# Author: Luiz Firmino

# Scope
# 3. Measure the time cost (efficiency) of an algorithm to use the computer’s clock to obtain an actual runtime. Via benchmarking/profiling implement an algorithm that counts from 1 to a million, time the algorithm and output the running time to the terminal window. Triple the problem size of this number and repeat this process. After four such increases, output the results of your program. For simplicity, measure the efficiency of the algorithm below.
# Start the algorithm
# work = 1
# for x in range(problemSize):
#       work += 5
#       work -= 5
# end of algorithm

import timeit
from datetime import datetime, timedelta

def main():

    problemSize = [1000000, 3000000, 9000000, 27000000]
    print("{:>20} {:>20}".format("Problem Size" , "Seconds"))
    for x in problemSize:
        start = datetime.now()
        work = 1
        for y in range(x):
            work += 5
            work -= 5
        
        print("{:>20} {:>20}".format(x , (datetime.now() - start).total_seconds()))
        
if __name__ == "__main__":
    main()