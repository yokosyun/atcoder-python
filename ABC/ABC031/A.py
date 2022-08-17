a, d = list(map(int, input().split()))
if a < d:
    print((a + 1) * d)
else:
    print(a * (d + 1))
