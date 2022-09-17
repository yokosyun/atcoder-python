n = int(input())
power = 1
for i in range(1, n + 1):
    power *= i
    power %= 1e9 + 7

print(int(power))