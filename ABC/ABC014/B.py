n, x = list(map(int, input().split()))
an = list(map(int, input().split()))

x_bin = format(x, "b").zfill(n)

total = 0
for ind in range(len(x_bin)):
    if x_bin[n - ind - 1] == "1":
        total += an[ind]
print(total)