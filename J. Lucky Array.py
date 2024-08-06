number=int(input())
n=list(map(int,input().split()))
minnum=min(n)
frequency=n.count(minnum)
if frequency%2==0:
    print("Unlucky")
else:
    print("Lucky")
