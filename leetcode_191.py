class Solution:
    def hammingWeight(self, n: int) -> int:
        s=''
        while n>0:
            n%=2
            s+=str(n)
            n//=2
        return s.count('1')
