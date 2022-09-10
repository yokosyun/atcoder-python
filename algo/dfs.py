# ABC/ABC054/C.py

# Depth First Search
def dfs(graph, now, done, num_nodes):
    cnt = 0
    if len(done) == num_nodes:
        return 1

    for target in graph[now]:
        if target not in done:
            cnt += dfs(graph, target, done + [target], num_nodes)
    return cnt


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


print(dfs(graph, 0, [0], n))
