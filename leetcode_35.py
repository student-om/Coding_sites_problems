class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        mid = (start + end )//2
        if nums[-1]<target:
            return len(nums)
        while start<end:
             
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end-=1
                mid=(start+end)//2
            else:
                start+=1
                mid=(start+end)//2
        return  mid            

