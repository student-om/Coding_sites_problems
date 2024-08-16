class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum_0=10000
        maximum_0=-10000
        minimum_1=10000
        maximum_1=-10000


        to_remove_0=0
        to_remove_1=0
        for i in range(len(arrays)):
            for j in arrays[i]:
                if j>maximum_0:
                    maximum_0=j
                    to_remove_0=i
        
                   
        a=arrays.copy()   #because python uses refrencing        
        arrays.remove(arrays[to_remove_0])
        
        for i in range(len(arrays)):
            for j in arrays[i]:
                if j<minimum_0:
                    minimum_0=j


        for i in range(len(a)):
            for j in a[i]:
                if j<minimum_1:
                    minimum_1=j
                    to_remove_1=i

        a.remove(a[to_remove_1])

        for i in range(len(a)):
            for j in a[i]:
                if j>maximum_1:
                    maximum_1=j
                   

        return max(abs(minimum_0-maximum_0),abs(minimum_1-maximum_1))
                     

    #first i found  greatest no maximum_0 then i removed the array containing greatest number
    #then i copied array
    #then i found least no of the copied array
    #then i removed array containing least number in the copied array
    #then i xompared abs(minimum_0-maximum_0) with (minimum_1-maximum_1)
    #and then i returned the highest value

                
        
