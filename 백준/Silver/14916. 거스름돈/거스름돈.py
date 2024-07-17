def min_coins(n):
    if n == 1 or n == 3:
        return -1

    count = 0
    while n > 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 2
        count += 1

    if n < 0:
        return -1

    return count

n = int(input())
print(min_coins(n))
