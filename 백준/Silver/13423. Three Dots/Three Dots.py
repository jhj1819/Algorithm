t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0

    numbers = list(map(int, input().split()))
    num_set = set(numbers)

    for i in range(n):
        for j in range(i+1, n):
            b = numbers[i] + numbers[j]
            if b % 2 !=0:
                continue
            if b//2 in num_set:
                answer += 1

    print(answer)