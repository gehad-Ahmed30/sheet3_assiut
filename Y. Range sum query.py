x,y=map(int,input().split())
n=list(map(int,input().split()))

prefix_sum=[0]*(x+1)  #prefix_sum = [0, 0, 0, 0, 0, 0, 0]
for i in range(1,x+1):
    prefix_sum[i]=prefix_sum[i-1]+n[i-1]    #prefix_sum[1] = prefix_sum[0] + A[0] = 0 + 6 = 6 [0, 6, 0, 0, 0, 0, 0]

for j in range(y):
    l,r=map(int,input().split())
    result = prefix_sum[r] - prefix_sum[l - 1]
    print(result)