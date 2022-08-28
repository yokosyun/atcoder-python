n = int(input())
an = list(map(int, input().split()))
cost = [0] * n
cost[1] = abs(an[1] - an[0])
for i in range(2, n):
    once = cost[i - 2] + abs(an[i - 2] - an[i])
    twice = cost[i - 1] + abs(an[i - 1] - an[i])
    cost[i] = min(once, twice)
print(cost[-1])
