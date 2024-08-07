def plusMinus(arr):
    # Write your code here
    positive=0
    negative=0
    zeros=0
    
    for i in arr:
        if i<0:
            negative+=1
            
        elif i>0:
            positive+=1
            
        else:
            zeros+=1    
            
    g=len(arr)
    positive=positive/g
    negative=negative/g
    zeros=zeros/g
    print(f"{positive:.6f}")
    print(f"{negative:.6f}")
    print(f"{zeros:.6f}")
