#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    a=0
    sum=0
    arr.sort()
    for i in arr:
        sum+=i
        
    min=sum-arr[4]
    max=sum-arr[0]
    print(min,  max)    
            
