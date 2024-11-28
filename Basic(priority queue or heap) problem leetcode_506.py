#priority queue example
import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        #stored -j bc heappop returns the smallest and i want largest to pop first for gold medal
        #so (- with largest no)=smallest no.
        #heapq is a class:
        #import and methods are heapq.heapify(object(list))->converts a list or any object into heap
        #heapq.heappop(object)->returns the smallest element from the heap
        #heapq.heappush(object,val)->pushes an object with a value onto the heap.
        max_heap=[(-j,i) for i,j in enumerate(score)]
        heapq.heapify(max_heap)
        answer=['']*n
        for rank in range(1,n+1):
            i,j=heapq.heappop(max_heap)
            if rank==1:
                answer[j]='Gold Medal'
            elif rank==2:
                answer[j]='Silver Medal'
            elif rank==3:
                answer[j]='Bronze Medal'
            else:
                answer[j]=str(rank)
        return answer
