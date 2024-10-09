class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        j=i+1
        p=[]
        while i<len(nums):
            temp=i
            j=i+1
            while j<len(nums) and nums[j]-nums[i]==1:
                j+=1
                i+=1
            if nums[i]==nums[temp]:
                p.append(str(nums[temp]))
            else:
                p.append(str(nums[temp]) + '->' + str(nums[i]))
            i=j

        return p
