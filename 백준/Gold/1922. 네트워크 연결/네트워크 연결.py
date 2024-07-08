#입력
v = int(input())
e = int(input())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [i for i in range(v+1)]

edges.sort()


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union_find(x,y):
    p = find(x)
    q = find(y)
    if p != q: 
        parent[p] = q
        return True
    return False

val = 0
connected_edge_num = 0
for edge in edges:
    if union_find(edge[1], edge[2]):
        val += edge[0]
        connected_edge_num += 1
    if connected_edge_num == v-1:
        break

print(val)