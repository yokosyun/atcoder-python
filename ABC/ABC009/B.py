n = int(input())
a = [int(input()) for _ in range(n)]
a = set(a)
a = sorted(a)
print(a[-2])
