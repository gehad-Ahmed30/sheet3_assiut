number=int(input())
for i in range(number):
    n=int(input())
    N=list(map(int,input().split()))
    count=0
    for x in range(n):
        for y in range(x,n):
            subarray=N[x:y+1]   #i=0 , j=0,1,2,3.....     #all subarray
            if all (subarray[k]<=subarray[k+1] for k in range(len(subarray)-1)):
                count+=1
    print(count)
        