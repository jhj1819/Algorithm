import sys
import heapq

input = sys.stdin.readline
answer = 0
n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a + b
    answer += c
    heapq.heappush(cards, c)

print(answer)