import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    val = list(map(int, input().split()))
    arr = [(i, val[i]) for i in range(n)]
    val.sort(reverse=True)

    i = 0
    count = 0

    while True:
        if arr[i][1] == val[count]:
            if arr[i][0] == m:
                print(count + 1)
                break
            count += 1

        else:
            arr.append((arr[i]))

        i += 1
