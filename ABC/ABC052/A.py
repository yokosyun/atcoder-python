a, b, c, d = list(map(int, input().split()))
ab = a * b
cd = c * d
if ab > cd:
    print(ab)
else:
    print(cd)