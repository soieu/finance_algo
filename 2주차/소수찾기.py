from itertools import permutations

# 소수
def Find_num(x:int):
    # 소수 판단 알고리즘
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    
    # 중복 값 제거 : set 사용
    lst = []
    for i in range(1, len(numbers)+1):
        for i in permutations(numbers, i):
            lst.append(int(''.join(i)))
    print(set(lst))
    
    answer = []
    for g in set(lst):
        if g > 1:
            aa = Find_num(g)
            answer.append(aa)
            
    return answer.count(True)  # True 값만 count