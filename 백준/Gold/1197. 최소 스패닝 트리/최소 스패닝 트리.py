#유니온 파인드?
#가중치 낮은거부터 정렬.
#유니온 파인드 연산..

#입력
v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

#기본 세팅 parent배열
parent = [i for i in range(v+1)]

#정렬 or 최소힙? 한번 정렬하면 계속 쓰니까 정렬?
edges.sort()


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union_find(x,y):
    p = find(x)
    q = find(y)
    if p != q: # 다를때만 유니온.
        parent[p] = q
        return True
    return False

val = 0
connected_edge_num = 0
#유니온파인드
for edge in edges:
    if union_find(edge[1], edge[2]):
        val += edge[0]
        connected_edge_num += 1
    if connected_edge_num == v-1:
        break

print(val)