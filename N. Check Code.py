x,y=map(int,input().split())
number=input().strip()
if len(number)!=x+y+1:
    print("No")
    exit()

if number[x]!= '-':
    print("No")
    exit()
for i in range(x):
    if not number[i].isdigit():
        print("No")
        exit()
for j in range(x+1,x+y+1):
    if not number[j].isdigit():
        print("No")
        exit()
print("Yes")