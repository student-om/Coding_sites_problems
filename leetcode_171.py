class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = {chr(i): i - 64 for i in range(65, 91)}
        ans=0
        res=0
        for i in range(len(columnTitle)-1,-1,-1):
            res+=dic[columnTitle[i]]*(26**ans)
            ans+=1
        return  res    
