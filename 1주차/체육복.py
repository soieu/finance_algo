def solution(n, lost, reserve):
    
    # 정렬
    lost.sort()
    reserve.sort()
    
    # 여벌 옷을 가지고 있는 사람 중 도둑 맞은 경우
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            
    # 앞/뒤 여벌 옷
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
            
        elif (r+1) in lost:
            lost.remove(r+1)
            
    return n - len(lost)
            