import sys
input = sys.stdin.readline

def cal_distance(a_spot, b_spot):
    ax, ay = a_spot
    bx, by = b_spot
    return round(pow(pow(ax - bx, 2) + pow(ay - by, 2), 1/2), 2)


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union_find(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root != b_root:
        parent[a_root] = b_root
        return True

    return False


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
    if union_find(a, b):
        count += 1
        answer += edge[0]
        if count >= n-1:
            print(answer)
            break




