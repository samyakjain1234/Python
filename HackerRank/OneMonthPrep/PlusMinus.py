#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    posCount,negCount,zeroCount = 0,0,0
    for i in arr:
        if i<0:
            negCount += 1
        elif i>0:
            posCount +=1
        else:
            zeroCount +=1
    
    print('{0:.6f}'.format(posCount/len(arr)))        
    print('{0:.6f}'.format(negCount/len(arr)))
    print('{0:.6f}'.format(zeroCount/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
