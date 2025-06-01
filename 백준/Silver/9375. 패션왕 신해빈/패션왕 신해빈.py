# (각 종류 수 +1) 들의 곱 - 1

t = int(input())

for _ in range(t):
    n = int(input())
    cloth_dict = dict()

    for i in range(n):
        name, category = input().split()
        if category not in cloth_dict:
            cloth_dict[category] = []
        cloth_dict[category].append(name)

    answer = 1
    for cloth_dict_key in cloth_dict:
        answer *= (len(cloth_dict[cloth_dict_key]) + 1)
    answer -= 1

    print(answer)