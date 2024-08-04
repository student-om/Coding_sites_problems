#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#Scenario 3: Indexing Mistake
#If you meant to use indices and arr is a list of lists but you accidentally used an element instead of an index, use index-based # #  access:
def diagonalDifference(arr):
    # Write your code here
    left=0
    right=0
    k=len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                left+=arr[i][j]
            
            
            if i+j==k-1 :   #for condition of the right diagonal, 2 if'd b/c i need to check for arr[1][1] for left and right diagonals
                right+=arr[i][j]
                
    return abs(left-right)           
                
