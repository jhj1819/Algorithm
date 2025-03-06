from itertools import combinations

while True:
    string_numbers = list(map(int, input().split()))
    if len(string_numbers) == 1:
        break
    string_numbers_except_len = string_numbers[1:]

    com_num = list(combinations(string_numbers_except_len, 6))
    for num in com_num:
        print(*num)
    print()