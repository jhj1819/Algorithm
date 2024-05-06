import heapq
import sys

input = sys.stdin.readline

n = int(input())
lecture_info_list = []
for _ in range(n):
    start, end = map(int, input().split())
    lecture_info_list.append((start, end))

lecture_info_list.sort(key=lambda x: x[0])

min_heap = []

for lecture_info in lecture_info_list:
    start, end = lecture_info[0], lecture_info[1]
    if min_heap and min_heap[0] <= start:
        heapq.heapreplace(min_heap, end)
    else:
        heapq.heappush(min_heap, end)

print(len(min_heap))
