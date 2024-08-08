import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    # Number of rows in the pattern
    num_rows = n

# Loop through each row
    for i in range(1, num_rows+1 ):
    # Calculate the number of spaces and stars
        spaces = ' ' * ((num_rows - i) )
        stars = '#' * i
    
    # Print the pattern with leading spaces and stars
        print(spaces + stars)

            
