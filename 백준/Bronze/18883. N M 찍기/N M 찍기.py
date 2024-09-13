N, M = map(int, input().split())
for i in range(1, N*M + 1):
    end_char = "\n" if i % M == 0 else " "
    print(i, end=end_char)

