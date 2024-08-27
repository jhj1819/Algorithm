import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
in_dict = dict()

for i in range(1, n + 1):
    in_dict[i] = 0

for _ in range(m):
    numbers = list(map(int, input().split()))
    for i in range(1, numbers[0]):
        adj_list[numbers[i]].append(numbers[i+1])
        in_dict[numbers[i+1]] += 1

queue = []
for i in range(1, n + 1):
    if in_dict[i] == 0:
        in_dict[i] -= 1  # 음수로 바꿔서 ==0 에 안걸리게
        queue.append(i)

answer = []
while queue:
    node = queue.pop()
    answer.append(node)
    for adj_node in adj_list[node]:
        in_dict[adj_node] -= 1
        if in_dict[adj_node] == 0:
            queue.append(adj_node)

for i in range(1, n+1):
    if in_dict[i] >0:
        print(0)
        exit(0)

for a in answer:
    print(a)
