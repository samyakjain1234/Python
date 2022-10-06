#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    res = []
    i=0
    for word in grid:
        #storing sorted char in list
        res.append(sorted(list(word))) 
        # stroing sorted transpose of list by using zip function
        care = list(map(list,zip(*res)))    
    while i < len(care):
        # returns No, if there is no match
        if care[i] != sorted(care[i]):      
            return 'NO'
        i += 1
    #else Yes, if everything matches.
    return 'YES'         

            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
