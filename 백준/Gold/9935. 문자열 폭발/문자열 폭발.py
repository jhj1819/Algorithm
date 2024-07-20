str = input()
boom = input()

n = len(boom)
last_boom = boom[-1]
stack = []
for c in str:
    stack.append(c)
    if c == last_boom:
        if len(stack) < n-1:
            continue
        if "".join(stack[-n:]) == boom:
            for _ in range(n):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")