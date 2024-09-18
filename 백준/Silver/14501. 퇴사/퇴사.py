n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)
for i in range(n):
    if i + arr[i][0] <= n:
        dp[i+arr[i][0]] = max(dp[i] + arr[i][1], dp[i+arr[i][0]])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])