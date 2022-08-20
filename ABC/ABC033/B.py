n = int(input())


max_val = 0
max_city = ""
total_val = 0
for _ in range(n):
    s, p = list(input().split())
    p = int(p)
    total_val += p
    if p > max_val:
        max_val = p
        max_city = s

if max_val > total_val / 2:
    print(max_city)
else:
    print("atcoder")
