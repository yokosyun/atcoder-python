def solve(ps, txa, txb, tya, tyb, max_dist):
    for p in ps:
        a = math.sqrt((p[0] - txa) ** 2 + (p[1] - tya) ** 2)
        b = math.sqrt((p[0] - txb) ** 2 + (p[1] - tyb) ** 2)
        dist = a + b
        if dist <= max_dist:
            return "YES"
    return "NO"


import math

txa, tya, txb, tyb, T, V = list(map(int, input().split()))
n = int(input())
ps = [list(map(int, input().split())) for _ in range(n)]


max_dist = T * V
print(solve(ps, txa, txb, tya, tyb, max_dist))