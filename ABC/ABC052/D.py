n, a, b = list(map(int, input().split()))
xn = list(map(int, input().split()))

total = 0
for idx in range(len(xn) - 1):
    dist = xn[idx + 1] - xn[idx]
    total += min(dist * a, b)

print(total)
