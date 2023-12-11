def solution(array, commands):
    answer = []
    for i in range(len(commands)): #담겨잇는만큼 반복
        i,j,k = commands[i][0], commands[i][1], commands[i][2]
        ex = array[i-1:j]
        ex.sort()   #sort함수는 오름차순 디폴트, 그 자체를 정렬, 반환값은 none
        answer.append(ex[k-1])
    return answer

#i-1 부터 j까지 인덱싱 후 정렬
#3번째 숫자 k-1 번째 숫자