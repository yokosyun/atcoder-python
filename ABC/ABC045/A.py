def main(a, b, h):
    y = (a + b) / 2 * h
    return int(y)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    h = int(input())
    res = main(a, b, h)
    print(res)
