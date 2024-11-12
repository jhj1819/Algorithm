import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
scores = dict()
for _ in range(N):
    a, b = map(int, input().split())
    if a not in scores:
        scores[a] = []
    scores[a].append(b)

pq = PriorityQueue()
answer = 0
max_day = max(scores)
for i in range(max_day, 0, -1):
    if i in scores:
        for s in scores[i]:
            pq.put(-s)
    if pq.qsize() >= 1:
        answer -= pq.get()

print(answer)
