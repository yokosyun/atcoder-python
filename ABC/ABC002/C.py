xa, ya, xb, yb, xc, yc = list(map(int, input().split()))

xb -= xa
yb -= ya
xc -= xa
yc -= ya
print(abs(xb * yc - xc * yb) / 2)
