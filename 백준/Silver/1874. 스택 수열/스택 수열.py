n = int(input())
targets = [int(input()) for _ in range(n)]
stack = []
t_idx, i = 0, 0
answer = ""

while t_idx < n:
    i += 1
    if i == targets[t_idx]:
        t_idx += 1
        answer += "+\n"
        answer += "-\n"
        continue

    if i > targets[t_idx]:
        if stack and stack[-1] == targets[t_idx]:
            stack.pop()
            t_idx += 1
            answer += "-\n"
            i -= 1
        else:
            answer = "NO"
            break
    else:
        stack.append(i)
        answer += "+\n"


print(answer)

