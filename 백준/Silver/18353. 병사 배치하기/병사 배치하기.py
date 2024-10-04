# 핵심: 열외 병사 수를 직접 계산하지말고, 전체 병사수에서 LIS값을 빼주는 방식
# dp[i] = 마지막이 i번 병사일 때 배치가능한 최대 병사 수
# dp점화식: 자기보다 높은 전투력을 보유한 병사들 중, 가장 큰 dp값

N = int(input())
power = list(map(int, input().split()))

dp = [1] * N   # 자기자신을 마지막으로 배치할 수 있음.

for i in range(N):
    for j in range(i):
        if power[j] > power[i]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = N - max(dp)
print(answer)