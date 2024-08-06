N, M = map(int, input().split())
A=[]
for i in range(N):
    A.append(input().strip())

X, Y = map(int, input().split())

X -= 1            #Convert 1-Based to 0-Based:   start=0
Y -= 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
flag_niegber = True

for dx, dy in directions:
    nx=X + dx    #X = 1, Y = 1, and dx = -1, dy = 0, then nx = 0 and ny = 1
    ny =Y + dy
    if 0 <= nx < N and 0 <= ny < M:
        if A[nx][ny] != 'x':
            flag_niegber= False
            break

if flag_niegber:
    print("yes")
else:
    print("no")
