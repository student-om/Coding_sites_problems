class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in ['(','{','[']:
                l.append(i)
            elif i in [')','}',']']:    
                if not l:
                    return False
                
                if (i==')' and l[-1]!='(') or (i=='}' and l[-1]!='{') or (i==']' and l[-1]!='['):
                    return False
                l.pop()

        if len(l)==0:
            return True    
