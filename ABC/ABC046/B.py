if __name__ == "__main__":
    input = input().split()
    n, k = list(map(int, input))
    res = k * (pow((k - 1), (n - 1)))
    print(res)
