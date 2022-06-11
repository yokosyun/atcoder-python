def main(input):
    for ind in range(len(input)):
        a = input[ind] + input[(ind + 1) % 3]
        b = input[(ind + 2) % 3]
        if a == b:
            return "Yes"
    return "No"


if __name__ == "__main__":
    input = input().split()
    input_list = list(map(int, input))
    res = main(input_list)
    print(res)