def solve(x):
    while len(x):
        if x[0] in ["o", "k", "u"]:
            x = x[1:]
        elif len(x) >= 2 and x[0:2] == "ch":
            x = x[2:]
        else:
            return "NO"
    return "YES"


x = input()

print(solve(x))