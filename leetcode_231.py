class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=bin(n)
        m={'1':'0','0':'1'}

        if n>0:
            if a.count('1')==1:
                return True
            else:
                return False
        else:
            sg=a.maketrans(m)
            sg=a.translate(sg)
            sg=str(eval('{}+1'.format('1000')))
            if sg.count('1')==1:
                return True
            else:
                return False
