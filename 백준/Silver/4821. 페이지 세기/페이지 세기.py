while True:
    n = int(input())
    if n == 0:
        break

    printed_page = [0] * (n+1)

    # 콤마로 나눠서 리스트에 넣기
    page_ranges = input().split(',')

    for page_range in page_ranges:
        if '-' not in page_range:  # 단일 페이지인 경우
            if int(page_range) <= n:
                printed_page[int(page_range)] = 1
        else:
            start, end = map(int, page_range.split('-'))
            for i in range(start, end + 1):
                # 초과되지 않는지 체크.
                if i > n:
                    break
                # print_page를 이용해서 중복 체크
                printed_page[i] = 1

    print(sum(printed_page[:n + 1]))
