import heapq 

def change_min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
    

def solution(book_time):
    answer = 0
    book_mins = [[change_min(time[0]), change_min(time[1])+9] for time in book_time]
    book_mins.sort()
    
    slot = []
    for book_min in book_mins:
        start_min, end_min = book_min[0], book_min[1]
        if len(slot) == 0 or slot[0] < start_min:
            if  len(slot) != 0:
                heapq.heappop(slot)
            heapq.heappush(slot, end_min)
        else:
            heapq.heappush(slot, end_min)

    return len(slot)

