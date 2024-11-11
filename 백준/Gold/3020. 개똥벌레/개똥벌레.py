import sys

input = sys.stdin.readline

n, h = map(int, input().split())
stalagmite = [0] * (h + 2)
stalactite = [0] * (h + 2)

for i in range(n//2):
    height = int(input())
    stalagmite[height] += 1
    height = int(input())
    stalactite[h - height + 1] += 1

for i in range(h - 1, 0, -1):
    stalagmite[i] += stalagmite[i + 1]

for i in range(2, h + 1):
    stalactite[i] += stalactite[i - 1]

min_obstacles = n
count = 0

for i in range(1, h + 1):
    obstacles = stalagmite[i] + stalactite[i]
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1
    elif obstacles == min_obstacles:
        count += 1

print(min_obstacles, count)
