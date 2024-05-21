n = int(input())
m = int(input())

adj_list = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False for _ in range(n+1)]

queue = []
visited[1] = True
queue.append(1)
count = 0
while queue:
    current = queue.pop(0)

    for next in adj_list[current]:
        if not visited[next]:
            visited[next] = True
            count += 1
            queue.append(next)

print(count)