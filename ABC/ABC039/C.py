from collections import Counter

onkai_mi = ["Mi", "Fa", "So", "La", "Si", "Do", "Re"][::-1]
onkai_si = ["Si", "Do", "Re", "Mi", "Fa", "So", "La"][::-1]

s = input()
for i in range(20 - 1):
    if s[i : i + 2] == "WW":
        index = i
        break

b_num = Counter(s[index + 2 : index + 7])["B"]
w_num = Counter(s[:index])["W"]

if b_num == 3:
    print(onkai_mi[w_num - 1])
elif b_num == 2:
    print(onkai_si[w_num - 1])
