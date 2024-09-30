number_sentence = input()
numbers = []
operators = []


def calc(a, b, o):
    if o == '-':
        return a - b
    if o == '+':
        return a + b
    if o == '*':
        return a * b
    if o == '/':
        return a // b  ## 파이썬 나누기 연산자


for n in number_sentence:
    if n in ('+', '-', '*', '/'):
        b = numbers.pop()  ## pop 순서 실수
        a = numbers.pop()
        c = calc(a, b, n)
        numbers.append(c)
    else:
        numbers.append(int(n))

print(numbers[0])
