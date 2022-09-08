from typing import List


def prime_factorize(n: int) -> List[int]:
    # print(prime_factorize(12))
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


def main():
    print(prime_factorize(12))


if __name__ == "__main__":
    main()