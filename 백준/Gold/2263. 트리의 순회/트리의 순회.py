import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

# 인덱스 배열
idx_list = [0] * (n+1)
for i in range(n):
    idx_list[inorder[i]] = i


def build_preorder(root_idx_postorder, left_idx_inorder, right_idx_inorder):
    global preorder
    # 잘못된 탐색인 경우 탈출  # 처음엔 ==인 경우와 구분했는데 어차피 ==이후의 build_preorder은 아래 조건문에 걸리므로 하나로..!
    if left_idx_inorder > right_idx_inorder:
        return

    # root_idx_inorder 구하기, find에서 시간소요가 클거같아.. 범위를 줄임 .. .그것도 안돼서 인덱스 맵or 인덱스배열..
    root_idx_inorder = idx_list[postorder[root_idx_postorder]]
    preorder.append(postorder[root_idx_postorder])  # 이때 탐색하는 순서가 pre_order가 된다.

    # 왼쪽 서브트리의 루트는 현재 root에서 왼쪽 서브트리 크기만큼 이동
    build_preorder(root_idx_postorder - (right_idx_inorder - root_idx_inorder + 1), left_idx_inorder,
                   root_idx_inorder - 1)
    # 오른쪽 서브트리의 루트는 바로 현재 root의 왼쪽
    build_preorder(root_idx_postorder - 1, root_idx_inorder + 1, right_idx_inorder)


build_preorder(n - 1, 0, n - 1)
print(' '.join(map(str, preorder)))