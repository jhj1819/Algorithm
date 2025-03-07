# dp[i][j][d] # d: 어디방향에서 온건지.. 0 위에서, 1 -> 2 <-

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-float('inf') for _ in range(3)] for _ in range(m)] for _ in range(n)]

dp[0][0][0] = grid[0][0]
dp[0][0][1] = grid[0][0]
dp[0][0][2] = grid[0][0]

for j in range(1, m):
    dp[0][j][1] = dp[0][j-1][1] + grid[0][j]

# 위에서 온거 계산, -> 계산 <- 계산

for i in range(1, n):
    for j in range(m):
        dp[i][j][0] = max(dp[i-1][j]) + grid[i][j]
    for j in range(1, m):
        dp[i][j][1] = max(dp[i][j-1][0:2]) + grid[i][j]
    for j in range(m-2, -1, -1):
        dp[i][j][2] = max(dp[i][j+1][0], dp[i][j+1][2]) + grid[i][j]

print(max(dp[n-1][m-1]))