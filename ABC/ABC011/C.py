def solve(n, ngs):
    cnt = 0
    if n in ngs:
        return "NO"
    while cnt < 100:
        cnt += 1
        if n - 3 not in ngs and n - 3 >= 0:
            n -= 3
        elif n - 2 not in ngs and n - 2 >= 0:
            n -= 2
        elif n - 1 not in ngs and n - 1 >= 0:
            n -= 1
        else:
            return "NO"
        if n == 0:
            return "YES"
    return "NO"


n = int(input())
ngs = [int(input()) for _ in range(3)]
print(solve(n, ngs))