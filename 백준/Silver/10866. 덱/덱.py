import sys
input = sys.stdin.readline

n = int(input())
cmd = [input().split() for _ in range(n)]

deque = []

for c in cmd:
    if c[0] == 'push_front':
        deque.insert(0, c[1])
    elif c[0] == 'push_back':
        deque.append(c[1])
    elif c[0] == 'pop_front':
        print(deque.pop(0) if deque else -1)
    elif c[0] == 'pop_back':
        print(deque.pop() if deque else -1)
    elif c[0] == 'size':
        print(len(deque))
    elif c[0] == 'empty':
        print(0 if deque else 1)
    elif c[0] == 'front':
        print(deque[0] if deque else -1)
    elif c[0] == 'back':
        print(deque[-1] if deque else -1)
