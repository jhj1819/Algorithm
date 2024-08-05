import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

dq = deque()
answer = 0
for i in range(n):
    dq.append(arr[i])
    while dq[-1] - dq[0] > k:
        dq.popleft()
    answer = max(answer, len(dq))

print(answer)