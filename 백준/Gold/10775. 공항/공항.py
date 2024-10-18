import sys

input = sys.stdin.readline


##  경로압축
def find(x):
    if next_gate[x] != x:
        next_gate[x] = find(next_gate[x])
    return next_gate[x]


g = int(input())
p = int(input())
next_gate = [i for i in range(g + 1)]

count = 0
for i in range(p):
    a = int(input())
    docking_gate = find(a)
    if docking_gate > 0:
        next_gate[docking_gate] = find(docking_gate - 1)  # 이전 번호 게이트의 next_gate 물려받기
        count += 1
    else:
        break

print(count)
