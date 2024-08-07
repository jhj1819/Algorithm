n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = A - B
print(len(C))
C_list = list(sorted(list(C)))
print(" ".join(map(str, C_list)))
