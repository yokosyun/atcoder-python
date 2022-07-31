N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]


def dfs(idx_n, xor):
    if idx_n == N:
        if xor == 0:
            return True
    else:
        for idx_k in range(K):
            if dfs(idx_n + 1, xor ^ T[idx_n][idx_k]):
                return True
        return False


if dfs(0, 0):
    print("Found")
else:
    print("Nothing")