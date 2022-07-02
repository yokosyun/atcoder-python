from collections import Counter


def is_correct(count_dict, is_even):
    for key, val in count_dict.items():
        if is_even:
            if key == 1:
                if val != 2:
                    return 0.0
            elif key % 2 == 1:
                if val % 2 != 0:
                    return 0.0
            else:
                return 0
        else:
            if key == 0:
                if val != 1:
                    return 0.0
            elif key % 2 == 0:
                if val % 2 != 0:
                    return 0.0
            else:
                return 0.0

    return (2 ** (n // 2)) % (10 ** 9 + 7)


if __name__ == "__main__":

    n = int(input())
    a = list(map(int, input().split()))
    count_dict = Counter(a)

    is_even = False
    if n % 2 == 0:
        is_even = True

    res = is_correct(count_dict, is_even)
    print(int(res))
