def solution(n, lost, reserve):
    
    answer = 0
    
    # 학생별 체육복 개수 리스트 생성
    gym_suit = [1] * (n)

    # 체육복 개수 현재 상황 담기
    for idx in lost:
        gym_suit[idx-1]-=1
    for idx in reserve:
        gym_suit[idx-1]+=1

    # 현재학생이 체육복이 없으면 먼저 앞의 학생에게 빌리고 앞의 학생이 없으면 뒤의 학생에게 빌림
    # 앞 -> 뒤 순서대로 해야 최대한으로 체육복을 분배할 수 있음
    for idx in range(n):
        if gym_suit[idx] == 0:
            if (idx > 0 and gym_suit[idx-1] == 2):
                gym_suit[idx] += 1
                gym_suit[idx-1] -= 1
            elif (idx < n - 1 and gym_suit[idx+1] == 2):
                gym_suit[idx] += 1
                gym_suit[idx+1] -= 1
    for i in gym_suit:
        if i > 0 :
            answer+=1
    return answer
