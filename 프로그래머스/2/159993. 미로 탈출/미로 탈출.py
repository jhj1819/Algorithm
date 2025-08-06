# S -> L 최단
# L -> E 최단
# 가중치없으므로 bfs 

from collections import deque
    

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                s = (i, j)
            if maps[i][j] == "L":
                l = (i, j)
            if maps[i][j] == "E":
                e = (i, j)
                
    def is_inside(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(start, target):
        dr = [0, 1, 0 ,-1]
        dc = [1, 0, -1, 0]
        visited = [[0 for j in range(m)] for i in range(n)]
        dq = deque([start])
        count = 0
        while dq:
            r, c = dq.popleft()
            if (r, c) == target:
                return visited[r][c]
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if is_inside(nr,nc) and maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                    dq.append((nr,nc))
                    visited[nr][nc] = visited[r][c] + 1
        return -1
    
    a = bfs(s, l)
    b = bfs(l, e)
    if a == -1 or b == -1:
        return -1
    
    return a + b