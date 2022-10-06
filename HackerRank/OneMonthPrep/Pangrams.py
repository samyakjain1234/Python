#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = ''.join(s.split()).lower()
    d = dict.fromkeys(string.ascii_lowercase,0)
    for char in s:
        d[char] += 1
    minValue = d.values()
    return "not pangram" if min(minValue) == 0 else "pangram"
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
