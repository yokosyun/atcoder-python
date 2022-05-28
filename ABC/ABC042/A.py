def check(x):
    if x == 5 or x == 7:
        True
    else:
        False


def main(a, b, c):
    if check(a) == False:
        return False
    if check(b) == False:
        return False
    if check(c) == False:
        return False

    if (a + b + c) == 17:
        return True
    else:
        return False


if __name__ == "__main__":
    input = input().split()

    res = main(int(input[0]), int(input[1]), int(input[2]))
    if res == True:
        print("YES")
    else:
        print("NO")
