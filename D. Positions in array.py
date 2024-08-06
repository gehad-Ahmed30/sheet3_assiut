number=int(input())
n=list(map(int,input().split()))

for i in n:
    if i<=10:
        print(f"A[{n.index(i)}] = {i}")