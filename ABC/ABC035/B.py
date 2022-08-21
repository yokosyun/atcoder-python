s = input()
t = int(input())


x = 0
y = 0
unknown = 0

for c in s:
    if c == "U":
        y += 1
    elif c == "D":
        y -= 1
    elif c == "L":
        x -= 1
    elif c == "R":
        x += 1
    else:
        unknown += 1

if t == 1:
    print(abs(x) + abs(y) + unknown)

else:
    res = abs(x) + abs(y) - unknown
    if res > 0:
        print(res)
    else:
        print(abs(res) % 2)
