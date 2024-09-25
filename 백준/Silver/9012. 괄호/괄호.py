n = int(input())

for _ in range(n):
    stack = []
    p_string = input()

    for p_char in p_string:
        if p_char == '(':
            stack.append(p_char)

        else:
            if len(stack) == 0:
                stack.append(p_char)
                break
            else:
                stack.pop()

    if stack:
        print('NO')
    else:
        print('YES')