import sys
input = sys.stdin.readline

s = input().rstrip()  
n = int(input())
left, right = list(s), []

for _ in range(n):
    command = input().rstrip()
    if command == 'L':
        if left:
            right.append(left.pop())
    elif command == 'D':
        if right:
            left.append(right.pop())
    elif command == 'B':
        if left:
            left.pop()
    else:  # 'P x' 형태
        _, char = command.split()
        left.append(char)

print(''.join(left + list(reversed(right))))