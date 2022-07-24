def solve(sort, s, n, k):
    changed = Counter()
    cnt = 0
    for ind in range(n):
        if sort[ind] != s[ind]:
            if changed[sort[ind]] == 0:
                changed[sort[ind]] += 1
                cnt += 1
            else:
                changed[sort[ind]] -= 1

            if changed[s[ind]] == 0:
                changed[s[ind]] += 1
                cnt += 1
            else:
                changed[s[ind]] -= 1

            if cnt > k:
                return sort[:ind] + s[ind:], cnt, ">k"
            elif cnt == k:
                return sort[: ind + 1] + s[ind + 1 :], cnt, "==k"

    return sort, cnt


from collections import Counter

n, k = map(int, input().split())
s = list(input())


sort = sorted(s)


res = solve(sort, s, n, k)
# print("".join(res))
print(res)