n = int(input())
numbers = list(map(int, input().split()))

stack = []
for i, number in enumerate(numbers):
    queue = []
    for _ in range(number):
        queue.append(stack.pop())

    stack.append(i+1)

    for _ in range(number):
        stack.append(queue.pop())

print(*stack)

