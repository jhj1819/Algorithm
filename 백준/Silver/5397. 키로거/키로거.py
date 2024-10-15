T = int(input())


def move_left_to_right(left_stack, right_stack):
    if left_stack:
        right_stack.append(left_stack.pop())
    pass


def move_right_to_left(left_stack, right_stack):
    if right_stack:
        left_stack.append(right_stack.pop())
    pass


for _ in range(T):
    keyboard_input = input()
    left_stack, right_stack = [], []
    for c in keyboard_input:
        if c == '<':
            move_left_to_right(left_stack, right_stack)
        elif c== '>':
            move_right_to_left(left_stack, right_stack)
        elif c == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(c)

    print("".join(left_stack + right_stack[::-1]))