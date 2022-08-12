def solve(A, n):
    if not sum(A) % n == 0:
        return -1

    ave = sum(A) // n
    ans = 0
    for i in range(n - 1):
        data = A[: i + 1]
        if (sum(data) / len(data)) != ave:
            ans += 1
    return ans


n = int(input())
A = list(map(int, input().split()))
print(solve(A, n))
