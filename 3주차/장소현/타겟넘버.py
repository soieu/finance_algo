from itertools import product

def solution(numbers, target):
    answer = 0
    temp = [(i, -i) for i in numbers]
    
    # product을 통해 중복 순열 구현
    for i in product(*temp):
        if sum(i) == target:
            answer += 1
            
    return answer
