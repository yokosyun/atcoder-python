n = int(input())
an = list(map(int, input().split()))

max_takahashi = -float("inf")
for i in range(n):
    max_aoki = -float("inf")

    for j in range(n):
        if j == i:
            continue

        t = an[min(i, j) : max(i, j) + 1]
        aoki = sum(t[1::2])

        if aoki > max_aoki:
            max_aoki = aoki
            takahashi = sum(t[::2])

    max_takahashi = max(takahashi, max_takahashi)

print(max_takahashi)
