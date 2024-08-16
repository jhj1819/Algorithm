from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

answer = n * (n - 1)
answer_idx = 0


def bfs(s):
    visited = [-1] * (n + 1)  # 방문 여부 및 거리를 기록하는 배열, -1은 방문하지 않음을 의미
    queue = deque([s])
    visited[0] = 0  # 1부터 시작이니까
    visited[s] = 0  # 자기 자신은 거리 0

    while queue:
        node = queue.popleft()

        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:  # 방문하지 않은 노드
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return sum([dist for dist in visited])


for i in range(1, n + 1):
    kebin_num = bfs(i)
    if answer > kebin_num:
        answer = kebin_num
        answer_idx = i

print(answer_idx)
