class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[]
        for i in range(len(nums)):
            if val != nums[i]:
                l.append(nums[i])
        for i in range(len(l)):
            nums[i]=l[i]
        return len(l)        
                    


