x = int(input())


a = x // 11
remain = x % 11
if remain == 0:
    b = 0
elif remain <= 6:
    b = 1
else:
    b = 2


print(a * 2 + b)
