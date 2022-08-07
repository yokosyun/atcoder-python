n, d, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]
ans = [-1] * k


def min_distance(l, r, s, t):
    if abs(r - st[i][1]) <= abs(l - st[i][1]):
        return r
    else:
        return l


for j, (l, r) in enumerate(lr):
    for i in range(k):
        if l <= st[i][0] <= r:
            if l <= st[i][1] <= r and ans[i] == -1:
                ans[i] = j + 1
            else:
                st[i][0] = min_distance(l, r, st[i][0], st[i][1])

for a in ans:
    print(a)