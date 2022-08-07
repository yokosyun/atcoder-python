s = list(input())
ans = ""
now = s.pop(0)
cnt = 1
while len(s):
    next = s.pop(0)
    if next == now:
        cnt += 1
    else:
        ans += now + str(cnt)
        cnt = 1
        now = next
ans += now + str(cnt)
print(ans)
