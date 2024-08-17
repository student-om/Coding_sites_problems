#unsolved
from typing import List

class Solution:
def maxPoints(self, points: List[List[int]]) -> int:
index_take = []
maximum_no_from_each_row = []
maximum = 0

for i in range(len(points)):
for j in points[i]:
if j > maximum:
maximum = j
index_take.append(points[i].index(maximum))
maximum_no_from_each_row.append(maximum)
maximum = 0

b = self.abs_finder(index_take) # Use 'self' to call the method
sum = 0

for i in maximum_no_from_each_row:
sum += i

return sum - b

def abs_finder(self, l):
sum = 0
for i in range(len(l) - 1):
sum += abs(l[i] - l[i + 1])
return sum
