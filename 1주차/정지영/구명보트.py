def solution(people, limit):
    
    # 정렬
    people.sort()
    
    # left/right index 지정
    left, right = 0, len(people)-1
    
    # 반복해서 해당되는 개수 찾기
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
            
        else:
            right -= 1
            answer += 1
            
    return (answer)
            