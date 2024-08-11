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
    # Write your code here
    if s.endswith('AM'):
        if s.startswith('12'):
            return s.replace(s[0:2], '00').removesuffix('AM')
        else:
            return s.removesuffix('AM')
        
    else:
        if s.startswith('12'):
            return s.removesuffix('PM')
        else:
            b=s[0:2]
            a=int(s[0:2])
            c=str(((12+a)% 24))
            return s.removesuffix('PM').replace(b, c)
