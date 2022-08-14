from collections import Counter

s = list(input())
c = Counter(s)
words = ["A", "B", "C", "D", "E", "F"]
res = ""
for word in words:
    res += str(c[word]) + " "
print(res[:-1])
