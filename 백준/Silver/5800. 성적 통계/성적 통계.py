n = int(input())

for i in range(n):
    scores = list(map(int,input().split()))[1:]
    scores.sort()
    gap = 0
    for j in range(len(scores)-1):
        gap = max(gap, scores[j+1] - scores[j])

    print(f"Class {i+1}")
    print(f"Max {scores[-1]}, Min {scores[0]}, Largest gap {gap}")
