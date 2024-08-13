#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        if grade >= 38:  # Only round if grade is 38 or more
            remainder = grade % 5
            if remainder >= 3:  # Round up if the difference is less than 3
                grade += (5 - remainder)
        rounded_grades.append(grade)  # Store the grade (rounded or not)
    
    return rounded_grades 
               
