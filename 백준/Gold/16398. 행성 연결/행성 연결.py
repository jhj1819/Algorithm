import heapq
import sys

input = sys.stdin.readline

n = int(input())

## 비용 인접행렬 배열 입력받음
costs = [list(map(int, input().split())) for _ in range(n)]

costs_heap = []
for i in range(1, n):  # 일단 0번행성부터 출발
    costs_heap.append((costs[0][i], i))  # (i로 가는 비용, i)
heapq.heapify(costs_heap)

visited = set()  #방문한 행성 번호 셋.
visited.add(0)

inf = float('INF')
dist = [inf for _ in range(n)]

count = 0
result = 0
while count < n-1:
    next_edge = heapq.heappop(costs_heap)
    if next_edge[1] not in visited:
        visited.add(next_edge[1])
        count += 1
        result += next_edge[0]
        for i in range(n):  # 방문하지 않는것들을 힙에 넣는다
            if i not in visited and costs[next_edge[1]][i] < dist[i]:
                dist[i] = costs[next_edge[1]][i]
                heapq.heappush(costs_heap, (costs[next_edge[1]][i], i))

print(result)