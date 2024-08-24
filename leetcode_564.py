class Solution:
    def nearestPalindromic(self, n):
        len_n=len(n)
        temp=len_n//2-1 if len_n%2==0 else len_n//2
        first_half=int(n[:temp+1])

        possibilities=[]
        possibilities.append(self.half_to_palindrome(first_half,len_n%2==0))
        possibilities.append(self.half_to_palindrome(first_half+1,len_n%2==0))
        possibilities.append(self.half_to_palindrome(first_half-1,len_n%2==0))
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10**len_n + 1)

        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)


    def half_to_palindrome(self,left:int,even:bool)->int:
        res=left
        if not even:
            left//=10        
        while left>0:
            res=res*10+left%10
            left//=10
        return res   
            

#123
#1
#res,left=12
#not even -> left=left//10->left=1
#12//10=1
#res=12*10+1%10=120+1=121


#1222
#i=1
#first half = int('12')=12
#res,left=12
#even -> pass if 
#res=12*10+12%10=122
#left=1
#res=122*10+1%10=1220+1=1221
#12+1=13
#res,left=13
#pass-if
#res=130+3=133
#left=1
#res=1330+1+1%10=1331
