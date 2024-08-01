import sys
input = sys.stdin.readline

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]


def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        parent[yroot] = xroot


n = int(input())
x, y, z = [], [], []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n - 1):
    edges.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

edges.sort()

parent = [i for i in range(n)]
count = 0
cost = 0
for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        cost += weight
        count += 1
        if count == n - 1:
            break

print(cost)
