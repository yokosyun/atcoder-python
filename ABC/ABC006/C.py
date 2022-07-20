def solve(n, m):
    for c in range(m + 1):
        b = -2 * c + m - 2 * n
        if b >= 0 and b <= m:
            a = n - b - c
            if a >= 0 and a <= m:
                return str(a) + " " + str(b) + " " + str(c)
    return "-1 -1 -1"


n, m = list(map(int, input().split()))
print(solve(n, m))
