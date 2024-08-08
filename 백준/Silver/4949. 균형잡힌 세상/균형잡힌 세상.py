while True:
    str = input()
    if str == ".":
        break
    stack = []
    for c in str:
        if c == ".":
            if stack:
                print("no")
            else:
                print("yes")
            break
        if c == '(' or c == '[':
            stack.append(c)

        if c == ')':
            if not stack or stack.pop() != '(':
                print("no")
                break
        if c == ']':
            if not stack or stack.pop() != '[':
                print("no")
                break


