a, b, c = list(map(int, input().split()))
ans = a * b * c % (10 ** 9 + 7)
print(ans)
