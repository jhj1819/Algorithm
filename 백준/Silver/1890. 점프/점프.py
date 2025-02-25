n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽 끝부터 좌->우로 ..
# 자기가 갈 수 있는 위치에 자기값 + 해주기.
# 범위 넘어가면 패스.
# 최정은 board[n-1][n-1]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i < i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]
        if j < j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]
print(dp[n-1][n-1])