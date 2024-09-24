def Z(n, r, c):
    if n == 0:
        return 0

    size = pow(2, n-1)

    num_elements_per_quadrant = size * size

    if r < size and c < size:  # 1 사분면
        return Z(n-1, r, c)
    elif r < size <= c:  # 2 사분면
        return num_elements_per_quadrant + Z(n-1, r, c - size)
    elif r >= size > c:  # 3 사분면
        return 2*num_elements_per_quadrant + Z(n-1, r-size, c)
    else:  # 4 사분면
        return 3*num_elements_per_quadrant + Z(n-1, r-size, c-size)


N, r, c = map(int, input().split())
print(Z(N, r, c))
