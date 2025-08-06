n = int(input())
book_sale = {}

for _ in range(n):
    name = input()
    book_sale[name] = book_sale.get(name, 0) + 1

# 최대 판매 수와 사전 순 최적 책을 동시에 탐색
max_count = -1
best_book = ""

for name in sorted(book_sale.keys()):  
    if book_sale[name] > max_count:
        max_count = book_sale[name]
        best_book = name

print(best_book)