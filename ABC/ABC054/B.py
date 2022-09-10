def solve(n, m, an, bn):
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if np.array_equal(bn, an[i : i + m, j : j + m]):
                return "Yes"
    return "No"


import numpy as np

n, m = list(map(int, input().split()))
an = [list(input()) for _ in range(n)]
bn = [list(input()) for _ in range(m)]
an = np.array(an)
bn = np.array(bn)


print(solve(n, m, an, bn))
