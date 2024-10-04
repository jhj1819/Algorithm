import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for _ in range(N):
    points = tuple(map(int, input().split()))
    max_dp[0], max_dp[1], max_dp[2] = max(max_dp[:2]) + points[0], max(max_dp) + points[1], max(max_dp[1:]) + points[2]
    min_dp[0], min_dp[1], min_dp[2] = min(min_dp[:2]) + points[0], min(min_dp) + points[1], min(min_dp[1:]) + points[2]

print(max(max_dp), min(min_dp))
