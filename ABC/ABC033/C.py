import numpy as np

s = input().split("+")

cnt = 0
for f in s:
    if "0" not in f.split("*"):
        cnt += 1
print(cnt)
