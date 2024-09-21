import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21 #특정한 값을 정하기보다 for문 내에서 몫 연산으로 거스를 수 있는 최대 조상을 구하는 방법은 안좋은가?
n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]
d = [0] * (n + 1)
c = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = True #방문여부를 나타는 배열을 추가하는게 이득인가?
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

def set_parent(): #dfs와 set_parent를 합치는건 가독성이 좋진 않지만 효율성은 좋은가?
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def LCA(a,b):
    #무조건 b 가 더 높음
    if d[a]> d[b]:
        a,b = b,a
    #깊이 일치
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i): # 2의 i승을 시프트 연산으로 나타냄(1 << i)
            b = parent[b][i]
    #조상으로 올라가며 찾기
    if a == b:
        return  a
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(LCA(a,b))