number=int(input())
n=list(map(int,input().split()))
x=n[::-1]         #slice reverse
print(f" ".join(map(str,x)))