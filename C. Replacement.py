number=int(input())
n=list(map(int,input().split()))
x=[]
for i in n:  
    if i>0:
        x.append(1)
    elif i<0:
        x.append(2)
    else:
        x.append(0)
print(' '.join(map(str,x)))
