from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = [list(input()) for i in range(R)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]


def available(nx, ny, cost):
    return (
        (0 <= nx < C)
        and (0 <= ny < R)
        and cost[ny - 1][nx - 1] == -1
        and field[ny - 1][nx - 1] == "."
    )


def bfs():
    cost = [[-1] * C for i in range(R)]
    que = deque()
    que.append((sy, sx))
    cost[sy - 1][sx - 1] = 0
    while len(que):
        py, px = que.popleft()
        if px == gx and py == gy:
            break
        for dx, dy in zip(dxs, dys):
            nx = px + dx
            ny = py + dy
            if available(nx, ny, cost):
                cost[ny - 1][nx - 1] = cost[py - 1][px - 1] + 1
                que.append((ny, nx))
    return cost[gy - 1][gx - 1]


print(bfs())
