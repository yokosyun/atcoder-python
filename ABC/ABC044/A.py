def main(n, k, x, y):
    if n >= k:
        sum = x * k + (n - k) * y
    else:
        sum = x * n
    return sum


if __name__ == "__main__":

    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    res = main(n, k, x, y)
    print(res)
