def lcs(A, B):
    lenA, lenB = len(A), len(B)
    dp = [0] * (lenB + 1)

    for i in range(1, lenA + 1):
        previous = 0
        for j in range(1, lenB + 1):
            temp = dp[j]
            if A[i - 1] == B[j - 1]:
                dp[j] = previous + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            previous = temp
    return dp[lenB]

A = input()
B = input()
print(lcs(A,B))
