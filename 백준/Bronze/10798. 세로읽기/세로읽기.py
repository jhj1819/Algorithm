s = ["" for _ in range(15)]

for _ in range(5):
    input_str = input()
    for i in range(len(input_str)):
        s[i] += input_str[i]

answer = ""
for s_ in s:
    answer += s_

print(answer)