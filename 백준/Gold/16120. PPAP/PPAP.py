str = input()
boom = ['P','P','A','P']
stack = []
for c in str:
    stack.append(c)
    if c == 'P':
        if len(stack) < 3:
            continue
        if stack[-4:] == boom:
            for _ in range(3):
                stack.pop()

print("PPAP" if len(stack) == 1 and stack[0] == 'P' else "NP")
