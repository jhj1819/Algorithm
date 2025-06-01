# 입력
n = int(input())


def fibo(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]


recursion_count = fibo(n)
dp_count = n - 2

# 출력
print(recursion_count, dp_count)