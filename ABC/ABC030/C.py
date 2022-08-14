n, m = list(map(int, input().split()))
x, y = list(map(int, input().split()))
an = list(map(int, input().split()))
bn = list(map(int, input().split()))

cnt = 0
time = 0
where = "a"

while (an and where == "a") or (bn and where == "b"):
    if where == "a":
        flight = an.pop(0)
        if flight >= time:
            time = flight + x
            where = "b"
    elif where == "b":
        flight = bn.pop(0)
        if flight >= time:
            time = flight + y
            where = "a"
            cnt += 1

print(cnt)
