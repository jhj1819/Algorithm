n = int(input())
responses = input()

bigdata_count = responses.count("bigdata")
security_count = responses.count("security")

if bigdata_count == security_count:
    print("bigdata? security!")
elif bigdata_count > security_count:
    print("bigdata?")
else:
    print("security!")
