x,y=map(int,input().split())
list_store=[]
for i in range(x):
    n=list(map(int,input().split()))
    list_store.append(n)               #[[1,3,2],[5,3,8]]
for j in list_store:       #هتلف على كل ليسته جوا الليسته الكبيره
    print(" ".join(map(str,j[::-1])))
