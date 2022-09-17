s, c = map(int, input().split())


ans = min(s, c // 2)
if c >= 2 * s:
    res = c - 2 * s
    ans += res // 4

print(ans)