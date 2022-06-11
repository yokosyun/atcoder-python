def main(input):
    vowels = ["a", "i", "u", "e", "o"]
    if input in vowels:
        return "vowel"
    else:
        return "consonant"


if __name__ == "__main__":
    input = input()
    res = main(input)
    print(res)
