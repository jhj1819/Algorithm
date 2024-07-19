h, w = map(int, input().split())
block = [int(a) for a in input().split()]
result = 0
i = 0
while i < w:
    is_found = False
    for level in range(block[i], -1, -1):
        for j in range(i + 1, w):
            if level <= block[j]:
                result += level*(j-i-1) - sum(block[i + 1:j])
                i = j
                is_found = True
                break
        if is_found:
            break
    if not is_found:
        i = i+1

print(result)
