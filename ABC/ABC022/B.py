from collections import Counter

n = int(input())
an = [int(input()) for _ in range(n)]

c = Counter(an)
res = 0
for _, val in c.items():
    res += val - 1
print(res)