max_val = -1
answer_r = 0
answer_c = 0
for i in range(1,10):
    numbers = list(map(int, input().split()))
    for j in range(1,10):
        if max_val < numbers[j-1]:
            max_val = numbers[j-1]
            answer_c = j
            answer_r = i

print(max_val)
print(answer_r, answer_c)

