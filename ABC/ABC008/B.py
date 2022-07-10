from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
s = Counter(s)
print(max(s, key=s.get))