number=int(input())
n=list(map(int,input().split()))
x=list(map(int,input().split()))

result1=sorted(n)
result2=sorted(x)

if result1==result2:
    print("yes")
else:
    print("no")