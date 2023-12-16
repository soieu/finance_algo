def solution(array, commands):
    answer = []

    for i, j, k in commands:
        sortedList = sorted(array[i-1:j])
        answer.append(sortedList[k-1])

    return answer