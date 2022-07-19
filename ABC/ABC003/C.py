n, k = list(map(int, input().split()))
rn = list(map(int, input().split()))
rn = sorted(rn)


rate = 0
for ind in range(k):
    rate += rn[n - k + ind]
    rate /= 2
print(rate)
