import sys

input = sys.stdin.readline
#입력
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    times = list(map(int, input().split()))

    next_list = [[] for _ in range(n+1)]
    in_degree = [[0, 0] for _ in range(n+1)] ##(남은작업수, 현재까지 소요된 시간)
    for _ in range(k):
        a, b = map(int, input().split())
        next_list[a].append(b)
        in_degree[b][0] += 1

    goal = int(input())
    is_goal = False
    queue = []
    for i in range(1, n+1): #초기에 진입차수 0인거 넣기
        if in_degree[i][0] == 0:
            if i == goal:
                print(times[i-1])
                is_goal = True
                break
            queue.append((i, 0))



    while not is_goal:
        node, curr_time = queue.pop(0) #후에 시간초과난다면 deque로 변경..
        curr_time = curr_time + times[node-1]  ##times 인덱스는 -1해줘야함
        ##print(f"{node}일 끝냄 소요시간 {curr_time}")
        for next_node in next_list[node]:
            in_degree[next_node][0] -= 1
            if in_degree[next_node][0] == 0:
                queue.append((next_node, max(in_degree[next_node][1], curr_time))) ##진입차수가 0이 되는 시점이 최대시간이 아니므로 또 최댓값을 계산해줘야함
                if next_node == goal:
                    print(max(in_degree[next_node][1], curr_time) + times[goal-1])
                    is_goal = True
                    break

            in_degree[next_node][1] = max(in_degree[next_node][1], curr_time) ##times 인덱스는 -1해줘야함