import io, os
from collections import deque

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

#입력
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    indegree = [0 for _ in range(n+1)]

    dp = [0 for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        pos = q.popleft()
        for i in graph[pos]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[pos] + time[i])
            if indegree[i] == 0:
                if i == w:
                    break
                q.append(i)

    print(dp[w])