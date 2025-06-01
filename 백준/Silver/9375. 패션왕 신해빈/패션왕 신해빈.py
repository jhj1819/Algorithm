# (각 종류 수 +1) 들의 곱 - 1

t = int(input())

for _ in range(t):
    n = int(input())
    cloth_dict = dict()
    lst = []

    for i in range(n):
        name, category = input().split()
        lst.append(category)
        if category not in cloth_dict:
            cloth_dict[category] = []
        cloth_dict[category].append(name)

    answer = 1
    lst = list(set(lst))
    for cloth_dict_key in lst:
        answer *= (len(cloth_dict[cloth_dict_key]) + 1)
    answer -= 1

    print(answer)