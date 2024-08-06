number=int(input())
n=list(map(int,input().split()))

maxnum=float('inf')
for i in n:
    flag=0
    while i%2==0:
        i//=2
        flag+=1
    maxnum=min(flag,maxnum)

    

print(maxnum)


