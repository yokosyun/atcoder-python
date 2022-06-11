def main(input_list):
    res = ""
    for x in input_list:
        res += x[0]
    return res


if __name__ == "__main__":
    input = input().split(" ")
    res = main(input)
    print(res)