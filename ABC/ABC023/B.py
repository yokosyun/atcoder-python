def n_1(left, right):
    return left == "a" and right == "c"


def n_2(left, right):
    return left == "c" and right == "a"


def n_0(left, right):
    return left == "b" and right == "b"


def solve(n, s):
    if n % 2 == 0:
        return -1

    middle_idx = (n - 1) // 2

    val = s[middle_idx]
    if val != "b":
        return -1

    cnt = 0
    for idx in range(1, middle_idx + 1):
        cnt += 1
        left = s[middle_idx - idx]
        right = s[middle_idx + idx]

        if cnt % 3 == 1:
            if not n_1(left, right):
                return -1
        elif cnt % 3 == 2:
            if not n_2(left, right):
                return -1
        else:
            if not n_0(left, right):
                return -1
    return cnt


n = int(input())
s = list(input())
print(solve(n, s))
