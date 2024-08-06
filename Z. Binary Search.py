x,y=map(int,input().split())
n=list(map(int,input().split()))   #time complexity o(n)

set_num=set(n)    # time complexity o(1)
for i in range(y):
    num_check=int(input())
    if num_check in set_num:
        print("found")
    else:
        print("not found")

           

    
