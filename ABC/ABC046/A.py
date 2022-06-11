def main(input_list):
    output_list = []
    for val in input_list:
        if val not in output_list:
            output_list.append(val)
    return len(output_list)


if __name__ == "__main__":
    input = input().split()
    input_list = list(map(int, input))
    res = main(input_list)
    print(res)
