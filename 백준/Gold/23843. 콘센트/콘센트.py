import heapq

n,m = map(int, input().split())
times = list(map(int, input().split()))

c = [0] * m

times.sort(reverse=True)

heapq.heapify(c)
for t in times:
    a = t + heapq.heappop(c)
    heapq.heappush(c, a)

print(max(c))