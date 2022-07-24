n = int(input())
diff = 2025 - n
for i in range(9):
    for j in range(9):
        if (i + 1) * (j + 1) == diff:
            print(str(i + 1) + " x " + str(j + 1))
