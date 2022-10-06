#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    c,result = 31,0
    arr,arr1,joinarr=[],[],[]
    while n!=0:
        res = 1 if n%2==0 else 0  #flipping it here only
        n = int(n/2)
        arr.append(res)
    joinarr = ([1] * (32-len(arr))) + arr[::-1] 
    for i in joinarr:
        result +=  i*(2**c)
        c-=1
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
