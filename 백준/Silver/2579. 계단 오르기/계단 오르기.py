import sys

input = sys.stdin.readline

n = int(input())
st = [0]
for _ in range(n):
    st.append(int(input().rstrip()))

dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = st[1]
if n == 1:
    print(dp[1])
    exit(0)
dp[2] = st[1] + st[2]
for i in range(3, n+1):
    dp[i] = max(st[i] + st[i-1] + dp[i-3], st[i] + dp[i-2])

print(dp[n])