from collections import Counter

n = int(input())
a = list(map(int, input().split()))
counter = Counter(a)

ans = len(counter)
evens = []

for k, v in counter.items():
    if v % 2 == 0:
        evens.append(k)

if len(evens) % 2 != 0:
    ans -= 1

print(ans)