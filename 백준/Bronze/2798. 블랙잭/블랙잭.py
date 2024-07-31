n, m = map(int, input().split())
points = list(map(int, input().split()))
answer = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = points[i] + points[j] + points[k]
            if sum <= m:
                answer = max(answer, sum)

print(answer)

