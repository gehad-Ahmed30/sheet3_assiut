number=int(input())
n=list(map(int,input().split()))
x=int(input())
try:
    y=n.index(x)
    print(y)
except:
    print(-1)

