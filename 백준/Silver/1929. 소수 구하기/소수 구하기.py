import math


def genPrimeNumList(start, end):
    primeNumList =[]
    for i in range(start,end+1):
        flag = True
        if i == 1:
            flag = False
        elif i == 2:
            flag = True
        else :
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    flag = False
                    break
        if(flag):
            primeNumList.append(i)

    return primeNumList


a,b = map(int,input().split())
primelist = genPrimeNumList(a,b)
for val in primelist:
    print(val)