T, W = map(int, input().split())
apples = [int(input()) for _ in range(T)]

# DP 테이블 초기화: prev_dp[w][pos], pos는 0(1번 나무) 또는 1(2번 나무)
prev_dp = [[-float('inf')] * 2 for _ in range(W + 1)]
prev_dp[0][0] = 0  # 시작 위치는 1번 나무(인덱스 0), 이동 0회

for a in apples:
    curr_dp = [[-float('inf')] * 2 for _ in range(W + 1)]
    a_idx = a - 1  # 나무 번호를 0 또는 1로 변환

    for w in range(W + 1):
        for pos in [0, 1]:
            if prev_dp[w][pos] == -float('inf'):
                continue

            # 이동하지 않는 경우
            new_w = w
            new_pos = pos
            gain = 1 if (new_pos == a_idx) else 0
            curr_dp[new_w][new_pos] = max(curr_dp[new_w][new_pos], prev_dp[w][pos] + gain)

            # 이동하는 경우
            new_w = w + 1
            if new_w > W:
                continue
            new_pos = 1 - pos  # 위치 변경
            gain = 1 if (new_pos == a_idx) else 0
            curr_dp[new_w][new_pos] = max(curr_dp[new_w][new_pos], prev_dp[w][pos] + gain)

    prev_dp = curr_dp

# 모든 가능한 경우 중 최대값 찾기
max_count = 0
for w in range(W + 1):
    for pos in [0, 1]:
        max_count = max(max_count, prev_dp[w][pos])

print(max_count)