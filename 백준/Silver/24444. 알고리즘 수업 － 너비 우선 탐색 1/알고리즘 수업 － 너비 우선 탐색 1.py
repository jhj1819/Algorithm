from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
adj_list = [[] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(n+1):
    adj_list[i].sort()

def bfs(r):
    visited = [False for _ in range(n+1)]
    dq = deque()
    dq.append(r)

    count_list = [0 for _ in range(n+1)]
    count = 0
    while dq:
        count += 1
        node = dq.popleft()
        count_list[node] = count
        visited[node] = True
        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                dq.append(adj_node)
                visited[adj_node] = True
    for i in count_list[1:]:
        print(i)
    return


bfs(r)
