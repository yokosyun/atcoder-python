m = int(input())
m = m / 1.0e3

if m < 0.1:
    print("00")
elif m <= 5:
    print(str(int(m * 10)).zfill(2))
elif m <= 30:
    print(int(m + 50))
elif m <= 70:
    print(int((m - 30) / 5 + 80))
else:
    print(89)