#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            if s[i+1:len(s)-i] == s[i+1:len(s)-i][::-1]:
                return i
            elif s[i:len(s)-1-i] == s[i:len(s)-1-i][::-1]:
                return len(s)-1-i
    return -1
                
            
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
