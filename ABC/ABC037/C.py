n, k = list(map(int, input().split()))
an = list(map(int, input().split()))
total = 0
for i in range(n):
    middle = min(i + 1, n - i)
    large = min(k, n - k + 1)
    num = min(middle, large)
    total += num * an[i]

print(total)
