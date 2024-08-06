number=int(input())
n=list(map(int,input().split()))
result_reverse=n[::-1]
if n==result_reverse:
    print("YES")
else:
    print("NO")