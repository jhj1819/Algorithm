import sys
input = sys.stdin.readline

n = int(input())

working_employees_set = set()

for _ in range(n):
    name, command = input().strip().split()
    if command == "enter":
        working_employees_set.add(name)
    else:
        working_employees_set.remove(name)

working_employees_list = list(working_employees_set)
working_employees_list.sort(reverse=True)

for employee in working_employees_list:
    print(employee)
