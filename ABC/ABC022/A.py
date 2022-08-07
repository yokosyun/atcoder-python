n, s, t = list(map(int, input().split()))
an = [int(input()) for _ in range(n)]
w = 0
cnt = 0
for a in an:
    w += a
    if s <= w <= t:
        cnt += 1
print(cnt)
