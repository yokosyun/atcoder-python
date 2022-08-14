n, m = list(map(int, input().split()))

# minutes
n = n % 12 * 5 + 5 * m / 60

# degree
m *= 6
n *= 6

ans = abs(m - n)
print(min(ans, 360 - ans))
