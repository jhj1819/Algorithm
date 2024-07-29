n, m = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])
start, end, result = 1, x[-1] - x[0], 0

##  거리를 기준으로...!

while end >= start:
    mid = (start + end) // 2

    count = 1
    value = x[0]
    for i in range(1, n):
        if x[i] >= value + mid:
            value = x[i]
            count += 1

    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
