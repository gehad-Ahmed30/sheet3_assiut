number=int(input())
for i in range(number):
    n=int(input())
    N=list(map(int,input().split()))
    result_list=[]
    for x in range(n):
        variable=N[x]
        for y in range(x,n):
            variable=max(variable,N[y])
            result_list.append(variable)
    print(" ".join(map(str,result_list)))