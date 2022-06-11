def main(num):
    sum = 0
    for ind in range(num):
        sum += ind + 1
    return sum


if __name__ == "__main__":
    input = input()
    res = main(int(input))
    print(res)
