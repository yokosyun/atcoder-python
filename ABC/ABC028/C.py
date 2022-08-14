import itertools

nums = list(map(int, input().split()))

A = list(map(sum, itertools.combinations(nums, 3)))
A.sort()
print(A[-3])