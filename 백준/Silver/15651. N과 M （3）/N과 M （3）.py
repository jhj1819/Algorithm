m,n = map(int,input().split())
def func(m,n,path):
    if len(path) == n:
        print(" ".join(map(str,path)))
        return
    for i in range(1,m+1):
        path.append(i)
        func(m,n,path)
        path.pop()

func(m,n ,[])