import bisect

n = int(input())
a = list(map(int,input().split()))
b = [a[0]]

for i in range(n):
    if a[i] > b[-1]:
        b.append(a[i])
    else:
        pos = bisect.bisect_left(b, a[i])
        b[pos] = a[i]


print(len(b))

