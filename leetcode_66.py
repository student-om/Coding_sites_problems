class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in range(len(digits)):
            ans=ans*10+digits[i]
        ans+=1
        l=[]

        while ans>0:
            l.append(ans%10)
            ans//=10
        return l[::-1]
            
