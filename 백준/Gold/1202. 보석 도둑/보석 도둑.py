import heapq
import sys

input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
max_weights = [int(input()) for _ in range(k)]

# 가격 내림차순 x , 무게 오름차순 #가방기준이니까 가격은 정렬 필요없구나..
jewels.sort(key=lambda x: x[0])
# 담을 수 있는 무게 오름차순
max_weights.sort()

total_value = 0  # 최종 값
max_heap = []  # 가방에 담을 수 있는 보석 가치
jewel_idx = 0  

for max_weight in max_weights:
    for i in range(jewel_idx, n):
        if jewels[i][0] <= max_weight:
            heapq.heappush(max_heap, -jewels[i][1])
            jewel_idx += 1
        else:
            break
            
    if max_heap:
        total_value -= heapq.heappop(max_heap)
        
print(total_value)