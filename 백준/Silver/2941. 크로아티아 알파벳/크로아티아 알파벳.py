s = input()

croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = 0
i = 0
while i < len(s):
    if i < len(s) - 2 and s[i:i+3] == "dz=":
        answer += 1
        i += 3
    elif i < len(s) - 1 and s[i:i+2] in croatian_alphabets:
        answer += 1
        i += 2
    else:
        answer += 1
        i += 1

print(answer)
