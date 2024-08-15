import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    dist_from_apple=s-a
    dist_from_orange=b-t
    apples_count=0
    oranges_count=0
    for i in range(len(apples)):
        if (apples[i]+a>=s) and (apples[i]+a<=t):
            apples_count+=1
            
    for i in range(len(oranges)):
        if oranges[i]+b >=s and oranges[i]+b<=t:
            oranges_count+=1  
            
    print(apples_count)
    print(oranges_count)  
