s = input()

for i, x in enumerate(s):
    if x == "A":
        start_cnt = i
        break

for i, x in enumerate(reversed(s)):
    if x == "Z":
        end_cnt = i
        break


print(len(s) - start_cnt - end_cnt)
