n, t = list(map(int, input().split()))
an = [int(input()) for _ in range(n)]

total = n * t

for idx in range(n - 1):
    interval = an[idx + 1] - (an[idx] + t)
    if interval < 0:
        total += interval
print(total)