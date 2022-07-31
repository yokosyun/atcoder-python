import numpy as np
import math

n = int(input())
an = list(map(int, input().split()))
res = []
for a in an:
    if a != 0:
        res.append(a)
print(math.ceil(np.mean(res)))