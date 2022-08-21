import numpy as np

n = int(input())
sn = [list(input()) for _ in range(n)]
sn = np.array(sn)

for idx in range(n):
    print("".join(sn[::-1, idx]))
