number=int(input())
list_array=[]
sum_num=0
sum_secned=0


for i in range(number):
    n=list(map(int,input().split()))
    list_array.append(n)
    
for x in range(number):
    sum_num+=list_array[x][x]
    sum_secned+=list_array[x][number-1-x]     #[4 - 1-0=3], [4-1-1=2]

result=abs(sum_num-sum_secned)   
print(result)

