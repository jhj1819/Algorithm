from itertools import combinations

s = input()

s_len = len(s)
cases = list(combinations(range(1, s_len), 2))  # 1,5 라면 중간 글자가 [1:5]

result = []
for case in cases:
    left, right = case
    new_s = s[:left][::-1] + s[left:right][::-1] + s[right:][::-1]
    result.append(new_s)

print(min(result))


