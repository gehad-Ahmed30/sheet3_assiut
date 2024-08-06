x,y=map(int,input().split())
list_2array=[]    # Initialize the 2D array


for i in range(x):
    n=list(map(int,input().split()))  #enter numbers
    list_2array.append(n)

z=int(input())     #number search  

flag_z=False       
for n in list_2array:
    if z in n:
           flag_z=True
if flag_z:
     print("will not take number")
else:
     print("will take number")