class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r=0,k
        total=sum(nums[l:r])
        max_avg=total/k
        if len(nums)<=k:
            return sum(nums)/len(nums)
        while r<len(nums):
            
            
            
            total+=nums[r]
            total-=nums[l]
            max_avg=max(max_avg,total/k)
            l+=1
            r+=1
        return max_avg
