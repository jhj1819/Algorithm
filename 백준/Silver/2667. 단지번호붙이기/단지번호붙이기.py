dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def dfs(r,c):

    if not graph[r][c]:
        return
    num[-1] += 1
    graph[r][c] = 0
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            dfs(nr, nc)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

num = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            num.append(0)
            dfs(i, j)


print(len(num))
num.sort()
for nu in num:
    print(nu)