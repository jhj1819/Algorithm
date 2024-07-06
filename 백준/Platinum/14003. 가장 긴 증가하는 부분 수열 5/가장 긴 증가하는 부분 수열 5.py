import bisect

n = int(input())
a = list(map(int,input().split()))
b = [a[0]]
lis_log = []

for i in range(n):
    if a[i] > b[-1]:
        b.append(a[i])
        lis_log.append((a[i], len(b)))
    else:
        pos = bisect.bisect_left(b, a[i])
        b[pos] = a[i]
        lis_log.append((a[i], pos + 1))

lis_len = len(b)
print(lis_len)

result =[]
for log in lis_log[::-1]:
    if log[1] == lis_len:
        result.append(log[0])
        lis_len -= 1

print(*result[::-1])
