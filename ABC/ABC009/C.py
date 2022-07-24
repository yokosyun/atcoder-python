from collections import Counter

N, K = map(int, input().split())
S = list(input())

s_sorted = sorted(S)
ans = ""

n_change = 0

for i in range(N):
    # unused words in next words
    remained_counter = Counter(S[: i + 1]) - Counter(ans)
    n_remained = sum(remained_counter.values())

    for char in s_sorted:
        is_unmatched = char != S[i]
        if is_unmatched + n_remained - (remained_counter[char] > 0) + n_change <= K:
            ans += char
            s_sorted.remove(char)
            n_change += is_unmatched
            break
print(ans)