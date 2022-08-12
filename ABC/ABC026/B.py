import math

n = int(input())
rn = [int(input()) for _ in range(n)]
rn.sort()
rn.reverse()

area = 0
for idx in range(n):
    r = rn[idx]
    if idx % 2 == 0:
        area += r ** 2
    else:
        area -= r ** 2

print(area * math.pi)
