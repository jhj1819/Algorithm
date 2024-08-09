# c와 n의 범위가 매우 작음..
# 배낭문제... 정렬이 필요한가? 분할되는 배낭은 정렬해야하지만 이건..
# 일단 배낭 구현하고... 최소를 구하는걸로?
# 확보된 메모리가 m을 넘어가면 멈추도록? 이렇게하려면 정렬필요
# c기준으론 정렬 할 필요가 있는데, 같은 c에대한 정렬은? 굳이..

n, m = map(int, input().split())
m_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

# 정렬시 꼬이지 않도록 두 리스트를 튜플로 묶어..
mc_list = [(c_, m_) for m_, c_ in zip(m_list, c_list)]

# 정렬 (정렬쉽게 c_를 앞에둠) (비용, 메모리)
mc_list.sort()

max_cost = 100*n+1
dp = [0] * max_cost

result = set()

for i in range(n):
    cost = c_list[i]
    mem = m_list[i]
    
    for j in range(max_cost - 1, cost - 1, -1):
        if dp[j - cost] != -1: 
            dp[j] = max(dp[j], dp[j - cost] + mem)

min_cost = float('inf')
for cost in range(max_cost):
    if dp[cost] >= m:
        min_cost = min(min_cost, cost)

print(min_cost)