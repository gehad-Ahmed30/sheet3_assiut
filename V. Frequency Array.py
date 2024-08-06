x, y = map(int, input().split())
n = list(map(int, input().split()))
count = [0] * (y + 1)
for num in n:
    count[num] += 1
for j in range(1, y + 1):
    print(count[j])
