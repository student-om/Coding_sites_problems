class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=dict.fromkeys([i for i in range(len(nums)+1)],0)
        i=len(nums)
        for i in nums:
            m[i]=m.get(i,0)+1
        for i in m:
            if m[i]==0:
                return i
