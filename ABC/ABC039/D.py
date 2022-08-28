def not_having_c(sn, i, j, h, w, dirs, c):
    for dir in dirs:
        idx = tuple(np.array(dir) + (i, j))
        if 0 <= idx[0] < h and 0 <= idx[1] < w:
            if sn[idx] == c:
                return False
    return True


def solve(sn, h, w):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    sn = np.array(sn)
    for i in range(h):
        for j in range(w):
            if sn[(i, j)] == "#":
                if not_having_c(sn, i, j, h, w, dirs, "."):
                    sn[(i, j)] = "o"

    for i in range(h):
        for j in range(w):
            if sn[(i, j)] == "#":
                if not_having_c(sn, i, j, h, w, dirs, "o"):
                    print("impossible")
                    return False

    print("possible")
    for s in sn:
        for j in range(w):
            s[j] = "#" if s[j] == "o" else "."
        print("".join(s))

    return True


import numpy as np

h, w = list(map(int, input().split()))
sn = [list(input()) for _ in range(h)]
solve(sn, h, w)