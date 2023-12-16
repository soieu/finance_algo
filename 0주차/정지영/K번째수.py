def solution(array, commands):
    answer = []
    
    for i in commands:
        
        extract = array[i[0]-1:i[1]]  # 숫자 인덱싱
        extract = sorted(extract)     # 정렬
        answer.append(extract[i[2]-1])
    
    return answer