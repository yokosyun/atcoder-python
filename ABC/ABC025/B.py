n, a, b = list(map(int, input().split()))

pos = 0
for _ in range(n):
    s, d = list(input().split())
    d = int(d)

    if d < a:
        d = a
    elif d > b:
        d = b

    if s == "East":
        pos += d
    else:
        pos -= d

if pos < 0:
    print("West", abs(pos))
elif pos > 0:
    print("East", pos)
else:
    print(0)
