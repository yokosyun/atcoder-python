from collections import Counter

ln = list(map(int, input().split()))
c = Counter(ln)

for key, val in c.items():
    if val % 2 == 1:
        print(key)