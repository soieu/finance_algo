def solution(n, lost, reserve):
    answer = 0

    lostStudent = list(set(lost) - set(reserve))
    reserveStudent = list(set(reserve) - set(lost))

    for r in reserveStudent:
        if r - 1 in lostStudent:
            lostStudent.remove(r - 1)
        elif r + 1 in lostStudent:
            lostStudent.remove(r + 1)

    answer = n - len(lostStudent)

    return answer