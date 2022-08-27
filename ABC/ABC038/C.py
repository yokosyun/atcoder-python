from math import factorial


def sum_of_arithmetic_progressions(a, d, n):
    return (n * (2 * a + (n - 1) * d)) / 2


n = int(input())
an = list(map(int, input().split()))

cnt = 0
total = n
for i in range(1, len(an)):
    if an[i] - an[i - 1] > 0:
        cnt += 1
    else:
        if cnt > 0:
            total += sum_of_arithmetic_progressions(1, 1, cnt)
        cnt = 0
if cnt > 0:
    total += sum_of_arithmetic_progressions(1, 1, cnt)


print(int(total))