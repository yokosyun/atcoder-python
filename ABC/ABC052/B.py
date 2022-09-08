n = int(input())
s = input()
total = 0
max_num = 0
for x in s:
    if x == "I":
        total += 1
    else:
        total -= 1
    max_num = max(max_num, total)
print(max_num)