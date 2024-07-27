score = input()
sum_score = 0

for c in score[:len(score)//2]:
    sum_score += int(c)
for c in score[len(score) // 2:]:
    sum_score -= int(c)

print("LUCKY" if sum_score == 0 else "READY")
