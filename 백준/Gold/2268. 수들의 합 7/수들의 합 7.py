import math
import sys

input = sys.stdin.readline
# 입력
n, m = map(int, input().split())

# 트리 초기화
# 트리 크기 구하기
tree_size = pow(2, math.ceil(math.log2(n)) + 1)
tree = [0 for _ in range(tree_size)]


def calc_range_sum(start_idx, end_idx):
    answer = 0
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            answer += tree[start_idx]  # 옆 부모로 넘어갈때 answer에 더해주기
            start_idx += 1
        if end_idx % 2 == 0:
            answer += tree[end_idx]
            end_idx -= 1
        start_idx //= 2
        end_idx //= 2

    return answer


for _ in range(m):
    a, b, c = map(int, input().split())
    b = b + tree_size // 2 - 1  # 트리 인덱스에 맞추기

    if a == 1:  # 변경
        diff = c - tree[b]
        while b > 0:
            tree[b] += diff
            b //= 2

    if a == 0:  # 구간합 출력
        c = c + tree_size // 2 - 1
        if b > c:
            b, c = c, b
        range_sum = calc_range_sum(b, c)
        print(range_sum)
