import math
import sys

input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

tree_size = pow(2, math.ceil(math.log2(n)) + 1)

min_tree = [0 for _ in range(tree_size)]
min_tree[tree_size // 2:tree_size // 2 + n] = numbers
for i in range(tree_size // 2 - 1, 0, -1):
    min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])


def calc_range_min(start_idx, end_idx):
    min_val = float('inf')
    while start_idx <= end_idx:
        if start_idx % 2 == 1:  # 시작 노드가 오른쪽 자식인 경우
            min_val = min(min_val, min_tree[start_idx])
            start_idx += 1
        if end_idx % 2 == 0:  # 끝 노드가 왼쪽 자식인 경우
            min_val = min(min_val, min_tree[end_idx])
            end_idx -= 1
        start_idx //= 2
        end_idx //= 2

    return min_val


for _ in range(m):
    b, c = map(int, input().split())
    b = b + tree_size // 2 - 1  # 트리 인덱스에 맞추기
    c = c + tree_size // 2 - 1
    range_min = calc_range_min(b, c)
    print(range_min)
