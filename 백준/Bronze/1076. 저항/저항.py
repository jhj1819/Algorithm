first_color = input()
second_color = input()
third_color = input()

dict1 = dict()
dict1["black"] = 0
dict1["brown"] = 1
dict1["red"] = 2
dict1["orange"] = 3
dict1["yellow"] = 4
dict1["green"] = 5
dict1["blue"] = 6
dict1["violet"] = 7
dict1["grey"] = 8
dict1["white"] = 9

answer = (dict1[first_color] * 10 + dict1[second_color]) * pow(10, dict1[third_color])

print(answer)