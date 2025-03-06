import sys
import copy

input = sys.stdin.readline

# 10줄의 입력 받기 (각 줄 10글자)
# 'O'는 켜짐, '#'는 꺼짐
grid = [list(input().strip()) for _ in range(10)]

# 전구 상태를 0과 1로 변환: 1이면 켜짐, 0이면 꺼짐
init = [[1 if grid[i][j] == 'O' else 0 for j in range(10)] for i in range(10)]

# 전구 상태를 반전시키는 함수 (토글)
def toggle(state, i, j):
    # (i, j)와 상하좌우
    for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 10 and 0 <= nj < 10:
            state[ni][nj] = 1 - state[ni][nj]  # 0 <-> 1

# 가능한 최소 누름 횟수를 저장 (초기값: 매우 큰 값)
min_press = float('inf')

# 첫 행에 대해 모든 2^10 경우의 수 브루트포스
for first_row_mask in range(1 << 10):
    # 원본 상태 복사 (deep copy)
    state = copy.deepcopy(init)
    press_count = 0

    # 첫 행에서의 누름 결정: j번째 비트가 1이면 (0, j) 스위치를 누른다.
    for j in range(10):
        if first_row_mask & (1 << j):
            toggle(state, 0, j)
            press_count += 1

    # 1행부터 9행까지 진행: 바로 위 행의 전구가 켜져 있으면 현재 행에서 같은 열을 눌러 끔.
    for i in range(1, 10):
        for j in range(10):
            if state[i-1][j] == 1:  # 위 행의 전구가 켜져 있다면
                toggle(state, i, j)
                press_count += 1

    # 마지막 행(9행)이 모두 꺼져 있는지 확인
    if all(state[9][j] == 0 for j in range(10)):
        min_press = min(min_press, press_count)

# 답 출력: 가능한 경우가 없으면 -1
print(min_press if min_press != float('inf') else -1)
