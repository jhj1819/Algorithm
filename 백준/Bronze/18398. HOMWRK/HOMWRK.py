t = int(input())
for _ in range(t):
    n = int(input())
    for _ in range(n):
        numbers = list(map(int, input().split()))
        print(numbers[0] + numbers[1], numbers[0] * numbers[1])