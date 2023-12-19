#한번에 최대 2명, 무게제한 - 최대한 적은 구명보트로 탈출
#최대한 큰 애들끼리 먼저 보내는게... 최소의 방법임  처음엔 일케 생각했는데 이건 사람 제한 없을때임
#큰애랑 작은애랑 보내는게 제일 최소 방법
from collections import deque
def solution(people, limit)
    cnt = 0
    #1) 일단 정렬하기 - 오름차순
    people = deque(sorted(people))
    
    while(len(people)1) #한명 남아있는건 따로 처리
        #2) 젤큰애+작은애 합한거 limit 안이면, 보내주기 아니면 큰애만 보내기
        if(people[0]+people[-1] = limit)
            cnt += 1
            people.pop()  #최대
            people.popleft()  #최소
        else
            cnt += 1
            people.pop()  #최대만 빼내기
    if(len(people)==1)
        cnt += 1
    return cnt