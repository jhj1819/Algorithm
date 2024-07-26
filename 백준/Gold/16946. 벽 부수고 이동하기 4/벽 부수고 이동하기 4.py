##  빈공간을 그룹별로 개수를 세고, 저장한다.

## 0,1은 문제에서 빈공간/벽으로 주어졌으므로, 구역번호는 2번부터 시작한다
##  ex)area_sizes = [0, 0]로 선언후 append로 추가.
## area_size[3] = x -> 3번 구역의 크기는 x이다.

# 방향 벡터 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, graph, current_area_num):
    queue = [(i, j)]
    current_area_size = 0

    while queue:
        x, y = queue.pop(0)
        graph[x][y] = current_area_num
        current_area_size += 1 # 구역 크기 증가

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = area_num

    return current_area_size

## 벽인부분 돌아가면서 주변에 있는 구역번호를 set()에 담음 (중복되지않게)
def calc_moves(x, y):
    adj_area_set = set()
    moves_after_break = 1 # 부순 자리도 갈 수 있음

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            adj_area_set.add(graph[nx][ny]) # 구역넘버를 집어넣음

    for size in adj_area_set:
        moves_after_break += area_sizes[size]

    return moves_after_break

##입력
n, m = map(int, input().split())
graph = []
answer_graph = []

for i in range(n):
    row = list(map(int, input()))
    graph.append(row)
    answer_graph.append(row[:])

# 구역 크기 리스트 초기화 및 구역 번호 시작 값 설정
area_sizes = [0, 0]
area_num = 2  # 구역 번호는 2번부터

# 빈 공간 구역 크기 계산/ graph 수종
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            area_sizes.append(bfs(i, j, graph, area_num))
            area_num += 1

# 벽인 부분 주변 구역 크기 합 계산
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer_graph[i][j] = calc_moves(i, j) % 10
##참고사항. area_size를 구하면서 기존의 graph가 변하므로 정답은 answer_graph에 적용해야함.

##출력
for row in answer_graph:
    for r in row:
        print(r, end="")
    print()