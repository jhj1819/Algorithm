import math
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def cal_distance(a_spot, b_spot):
    ax, ay = a_spot
    bx, by = b_spot
    return math.sqrt(pow(ax - bx, 2) + pow(ay - by, 2))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


n = int(input())
spot = []
for i in range(n):
    a, b = map(float, input().split())
    spot.append((a, b))

edges = []
for i in range(n):
    for j in range(i+1, n):
        dis = cal_distance(spot[i], spot[j])
        edges.append((dis, i, j))

edges.sort()

parent = [i for i in range(n)]
count = 0
answer = 0
for edge in edges:
    a, b = edge[1], edge[2]

    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root != b_root:
        parent[a_root] = b_root
        count += 1
        answer += edge[0]
        if count >= n-1:
            print(round(answer, 2))
            break




