import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

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

v, e = map(int, input().split())

parent = [i for i in range(v+1)]
edges = []
is_cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if not union_find(a,b):
        print(i+1)
        is_cycle = True
        break

if not is_cycle:
    print(0)
