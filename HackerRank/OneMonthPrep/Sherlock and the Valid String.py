#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    list1 = Counter(s)
    values = sorted(list(list1.values()))
    n = len(values)
    # To check if there is only one character
    if n == 1:         
        return 'YES'
    #to check if first value is 1 and the second most value contains max value of list
    elif values[0] == 1 and values[1] == max(values):     
        return 'YES'
    #to check if first value and last value of list is same
    elif values[0] == max(values):
        return 'YES'
    #to check first value and last second value contains same value and last value same as first value.
    elif  values[0] == values[n-2] and values[n-1] - 1 == values[0]:
        return 'YES'
    #returns No , if no condition is matched.
    else:
        return 'NO'       
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
