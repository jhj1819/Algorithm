from collections import deque


def bfs(start_positions, graph, initial_keys):
    dq = deque(start_positions)
    keys = set(initial_keys)
    visited = set(start_positions)
    doors = {}
    documents = 0

    while dq:
        x, y = dq.popleft()
        cell = graph[x][y]

        if cell == '*':
            continue
        elif cell == '$':
            documents += 1
        elif cell.islower():  # 열쇠를 찾은 경우
            keys.add(cell)
            # 이 열쇠에 해당하는 문이 대기 중이라면 탐색 재개
            if cell.upper() in doors:
                for door_pos in doors[cell.upper()]:
                    dq.append(door_pos)
                del doors[cell.upper()]
        elif cell.isupper():  # 문을 만난 경우
            if cell.lower() not in keys:
                doors.setdefault(cell, []).append((x, y))
                continue  # 현재 문을 열 수 없으므로 계속

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and (nx, ny) not in visited and graph[nx][ny] != '*':
                visited.add((nx, ny))
                dq.append((nx, ny))

    return documents


def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n, m = map(int, input().split())
        graph = [input() for _ in range(n)]
        keys_input = input().strip()
        initial_keys = set(keys_input) if keys_input != '0' else set()

        # 건물 입구 찾기
        start_positions = [(i, j) for i in range(n) for j in range(m) if i == 0 or i == n - 1 or j == 0 or j == m - 1 if
                           graph[i][j] != '*']

        result = bfs(start_positions, graph, initial_keys)
        results.append(result)

    for res in results:
        print(res)


solve()
