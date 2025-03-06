import sys

input = sys.stdin.readline

T, W = map(int, input().split())

fruit_pos = []
for _ in range(T):
    fruit_pos.append(int(input()))

dp = [[[0 for _ in range(W + 1)] for _ in range(3)] for _ in range(T)]
# dp[i][j][k]: i: 초 j: 현재위치 k: 이동횟수
for i in range(T):
    gain_1 = 1 if fruit_pos[i] == 1 else 0
    gain_2 = 1 if fruit_pos[i] == 2 else 0
    for j in range(W + 1):
        if i == 0:
            dp[i][2][1] = gain_2
            dp[i][1][0] = gain_1
            continue
        if j == 0:
            dp[i][1][0] = dp[i-1][1][0] + gain_1
            continue
        dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][2][j - 1]) + gain_1
        dp[i][2][j] = max(dp[i - 1][2][j], dp[i - 1][1][j - 1]) + gain_2
        # j가 0 일때 이경우는 선택되지 않을거라 생각했는데 아니었음
        # j 가 너무 길어지지 않도록 끊어줄 필요도 있겠다


print(max(max(dp[T - 1][1]), max(dp[T - 1][2])))
