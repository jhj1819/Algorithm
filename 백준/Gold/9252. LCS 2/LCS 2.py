import sys     
sys.setrecursionlimit(10000)

def lcs(A, B):
    lenA, lenB = len(A), len(B)
    dp = [[0] * (lenB+1) for _ in range(lenA+1)]

    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def traceback(i, j, A, B, dp):
    if i == 0 or j == 0 :
        return ""
    if A[i-1] == B[j-1]:
        return traceback(i - 1, j - 1, A, B, dp) + A[i-1]
    elif dp[i][j-1] >= dp[i-1][j]:
        return traceback(i, j-1, A, B, dp)
    else:
        return traceback(i-1, j, A, B, dp)


A = input()
B = input()
dp = lcs(A,B)
print(dp[len(A)][len(B)])
print(traceback(len(A), len(B), A, B, dp))


