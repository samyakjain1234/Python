#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    arr = s.split(':')
    #check 12 and AM or PM
    if arr[0] == '12' and 'PM' in arr[2]:
        print((":".join(arr)).replace('PM',''))
    elif arr[0] == '12' and 'AM' in arr[2]:
        arr[0] = "00"
        print((":".join(arr)).replace('AM',''))
    else:
        if 'PM' in arr[2]:
            arr[0] = int(arr[0])
            arr[0] = str(12+arr[0])
            print((":".join(arr)).replace('PM',''))
        else:
            print((":".join(arr)).replace('AM',''))
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    #result = timeConversion(s)

    timeConversion(s)
    #fptr.write(result + '\n')

    #fptr.close()
