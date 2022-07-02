"""
eraser or earas + erase
dreamer or drame + erase
"""

s = input()
t = ""

idx = 0
fi = ["dream", "erase"]
si = "eraser"
se = "dreamer"

res = "NO"

while idx < len(s):

    if s[idx : idx + 6] == si and (
        (idx + 9 < len(s) and s[idx + 6 : idx + 9] != "ase") or idx + 6 == len(s)
    ):

        idx += 6

    if s[idx : idx + 6] == si and (
        (idx + 9 < len(s) and s[idx + 6 : idx + 9] != "ase") or idx + 6 == len(s)
    ):
        idx += 7

    elif s[idx : idx + 5] in fi:
        idx += 5

    else:
        res = "NO"
        break

    if idx == len(s):
        res = "YES"
        break

print(res)
