def solution(sizes):
    s = []
    b = []

    # 명함의 가로, 세로 길이 중 작은 쪽은 s, 큰 쪽에 b
    for size in sizes:
        s.append(min(size))
        b.append(max(size))
    
    # 모든 명함을 수납하기 위해 각 배열의 최댓값 추출
    return max(s) * max(b)