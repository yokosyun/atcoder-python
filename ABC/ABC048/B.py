if __name__ == "__main__":
    input = list(map(int, input().split()))
    first = (input[0] - 1) // input[2]
    second = input[1] // input[2]
    print(second - first)
