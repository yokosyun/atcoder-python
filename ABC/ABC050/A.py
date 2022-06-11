def main(inputs):
    if inputs[1] == "+":
        return int(inputs[0]) + int(inputs[2])
    else:
        return int(inputs[0]) - int(inputs[2])


if __name__ == "__main__":
    input = input().split()
    res = main(input)
    print(res)
