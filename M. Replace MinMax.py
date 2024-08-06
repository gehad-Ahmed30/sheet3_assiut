number=int(input())
n=list(map(int,input().split()))

minnum=min(n)
maxnum=max(n)
x=[]
for i in range(number):
    if n[i]==minnum:
        x.append(maxnum)
    elif n[i]==maxnum:
        x.append(minnum)
    else:
        x.append(n[i])
print(" ".join(map(str,x)))