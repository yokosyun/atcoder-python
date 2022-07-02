def all_divisible(dic, div_factor):
    for key in dic:
        if (dic[key] % div_factor) == 1:
            return "No"
    return "Yes"


if __name__ == "__main__":
    from collections import Counter

    input = input()
    dic = Counter(input)
    print(all_divisible(dic, 2))
