sum = 0
for _ in range(3):
    s, e = list(map(int, input().split()))
    sum += s * e / 10
print(int(sum))
