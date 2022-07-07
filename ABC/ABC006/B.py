Sequence = [float("inf") for _ in range(1000000 + 1)]
Sequence[0] = 0
Sequence[1] = 0
Sequence[2] = 0
Sequence[3] = 1


def tribonacci_h(n):

    for i in range(4, n + 1):
        Sequence[i] = (Sequence[i - 3] + Sequence[i - 2] + Sequence[i - 1]) % 10007
    return Sequence[n]


n = int(input())
print(tribonacci_h(n))
