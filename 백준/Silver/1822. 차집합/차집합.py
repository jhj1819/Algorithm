n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = A - B
print(len(C))
if len(C) > 0:
    C_list = list(C)
    C_list.sort()
    print(*C_list)