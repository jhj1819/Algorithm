import sys

sys.setrecursionlimit(10 ** 7)


def dfs(node):
    depth = 1
    x, y = node
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            depth += dfs((nx, ny))

    return depth


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer, count = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            answer = max(answer, dfs((i, j)))

print(count)
print(answer)
