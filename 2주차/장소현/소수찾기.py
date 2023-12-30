from itertools import permutations
import math 

def solution(numbers):
    answer = []
    count = 0
    
    # 종이 조각으로 나올 수 있는 숫자
    for i in range(len(numbers)):
        per = permutations(list(numbers), i+1)
        
        for p in per:
            num = int("".join(p))
            
            if num not in answer:
                answer.append(num)
            
    m = max(answer)
    
    # 에라토스테네스의 체
    prime = [False, False] + [True] * (m-1)
    
    # 2부터 m의 제곱근까지 확인 
    for i in range(2, int(math.sqrt(m))+1):
        if prime[i]:
            # i를 제외한 i의 모든 배수 지우기
            j = 2
            while i*j <= m:
                prime[i*j] = False
                j += 1
    
    # 소수 개수 출력   
    for i in answer:
        if prime[i]:
            count += 1

    return count