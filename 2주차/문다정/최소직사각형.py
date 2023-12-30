def solution(sizes):
    answer = 0
    garo, sero = [],[]
    for i in sizes:
        garo.append(min(i))
        sero.append(max(i))
    return max(garo)*max(sero)


#주어진 명함들을 다 넣되, 그 명함지갑의 면적이 최소가 되도록
#문제에서의 가로/세로 개념을 버리고, 무조건 가로는 짧은, 세로는 긴 형태로 명함들을 모은다고 생각