from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f ** 2 <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())

counters = Counter()
for i in range(2, n + 1):
    c = Counter(prime_factorize(i))
    counters += c

ans = 1
for num in counters.values():
    ans *= num + 1
ans %= 10 ** 9 + 7
print(ans)