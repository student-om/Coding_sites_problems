class Solution:
    def toHex(self, num: int) -> str:
        m={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        a=''
        b=[]
        c=abs(num)
        if num==0:
            return '0'
        if num>0:
            while num>0:
                rem=num%16
                num=num//16
                a+=str(m[rem])
        
        else:
            while c>0:
                b.append(c%2)
                c//=2
            while len(b)<32:
                b.append(0)
            ones_comp=[1-bit for bit in b]
            carry=1
            for i in range(len(ones_comp)):
                new_bit=ones_comp[i]+carry
                if new_bit==2:
                    ones_comp[i]=0
                    carry = 1
                else:
                    ones_comp[i]=new_bit
                    carry=0
            temp=0
            for i in range(len(ones_comp)):
                temp+=ones_comp[i]*(2**i)
            while temp>0:
                rem=temp%16
                temp=temp//16
                a+=str(m[rem])
        return a[::-1]

            
        
