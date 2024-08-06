number=int(input())
n=list(map(int,input().split()))
x=min(n)
print(f"{x} {n.index(x)+1}")
    