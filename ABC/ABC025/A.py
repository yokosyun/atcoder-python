s = list(input())
n = int(input())
length = len(s)
i = (n - 1) // length
j = (n - 1) % length

print(s[i] + s[j])
