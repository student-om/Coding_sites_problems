class Solution:
    def isHappy(self, n: int) -> bool:
        mydict={}
        while n!=1:
            ans=0
            original=n
            
            while n>0:
                rem=n%10
                ans+=rem**2
                n//=10
            mydict[original]=mydict.get(original,0)+1
            if mydict[original]>1:
                return False
            n=ans
        return True
            

