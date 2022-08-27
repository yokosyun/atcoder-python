import numpy as np

n, q = list(map(int, input().split()))
data = np.zeros(n)

for _ in range(q):
    l, r, t = list(map(int, input().split()))
    data[l - 1 : r] = t
for a in data:
    print(int(a))