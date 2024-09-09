count = 0
log_set = set()
n = int(input())

for _ in range(n):
    log = input()
    if log == 'ENTER':
        log_set.clear()
    else:
        if log not in log_set:
            count += 1
            log_set.add(log)

print(count)
