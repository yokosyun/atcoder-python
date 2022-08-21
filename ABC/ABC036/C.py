from collections import Counter

n = int(input())
an = [int(input()) for _ in range(n)]
nums = sorted(set(an))

dic = {}
for i, (k) in enumerate(nums):
    dic[k] = i

for a in an:
    print(dic[a])