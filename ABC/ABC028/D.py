import itertools

n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]
ans = ((n - k) * (k - 1) * 6 + (n - 1) * 3 + 1) / (n ** 3)
print(ans)
