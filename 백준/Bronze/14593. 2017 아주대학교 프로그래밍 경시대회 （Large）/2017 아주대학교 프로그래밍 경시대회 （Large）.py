n = int(input())
arr = []

for i in range(n):
    a, b, c = map(int,input().split())
    arr.append((a, -b, -c, i+1))

arr.sort(reverse=True)

print(arr[0][3])