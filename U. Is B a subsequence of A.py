x,y=map(int,input().split())      #number size array, number size sequence
a=list(map(int,input().split()))  #number array
b=list(map(int,input().split()))  #number sequence
j,i=0,0

while i<x and j<y:      

       if a[i]==b[j]:      
           j+=1
       i+=1            #هيزيد في حاله لو if متحققش ونلف تانى فى اللوب
if j==y:
    print("YES")
else:
    print("NO")