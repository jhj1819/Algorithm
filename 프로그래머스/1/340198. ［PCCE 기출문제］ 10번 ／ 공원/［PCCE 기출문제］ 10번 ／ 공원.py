# 큰 돗자리부터, 시작점을 기준으로 정사각형을 펼칠 수 있는지 확인.
# check_area(시작점튜플), 길이.)... 시작점튜플은 0~ n-길이

# 정렬
# 큰 크기부터 유효한지 확인 -> 유효하면 바로 반환
# 작은거까지 모두 유효하지 않다면.. -1 

# 불가능하면 False, 가능하면 True
def check_area(mat_len, park): # n: 공원길이, m: 돗자리길이 
    park_h = len(park) # 공원 세로.
    park_w = len(park[0]) # 공원 가로
    for i in range(0, park_h - mat_len + 1):
        for j in range(0, park_w - mat_len + 1):
            if check_valid((i,j), mat_len, park):
                return True
    return False

def check_valid(spot, mat_len, park):
    i,j = spot
    for ii in range(i, i + mat_len):
        for jj in range(j, j + mat_len):
            ##print(f"park[{ii}][{jj}] = {park[ii][jj]}")
            if park[ii][jj] != "-1":
                return False
    return True
 
def solution(mats, park):
    answer = -1
    
    
    mats.sort(reverse = True)
    
    for mat_len in mats:
        if check_area(mat_len, park):
            answer = mat_len
            break
    
    
    return answer