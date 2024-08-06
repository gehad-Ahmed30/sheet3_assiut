number=int(input())

start=0
end=1
if number==1:
    print(0)
elif number==2:
    print(1)
else:
    for i in range(3,number+1):
     x=start+end
     start=end
     end=x
    print(x)
