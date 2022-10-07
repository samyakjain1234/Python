#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):     #main method
    # Write your code here
    turn = ['Louise','Richard']
    chance = 1
    while(n>1):
        if isPowerOfTwo(n):
            n = n/2
        else:
            n = n  - nearestPower(n)
        chance  =  1 if chance == 0 else 0     
    return turn[chance]
             
    
def isPowerOfTwo(n):     #to cbeck power of two 
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
 
    return True         

def nearestPower(num):          #to check nearest Power of 2
    p = int(math.log(num,2))
    return int(pow(2,p))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
