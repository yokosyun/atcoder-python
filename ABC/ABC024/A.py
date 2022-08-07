a, b, c, k = list(map(int, input().split()))
s, t = list(map(int, input().split()))

if s + t >= k:
    a -= c
    b -= c

res = a * s + b * t
print(res)
