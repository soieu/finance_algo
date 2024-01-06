answer = 0

def bt(numbers, idx, value, target):
    global answer 
    if idx == len(numbers):
        if value == target:
            answer += 1
        return
    bt(numbers, idx + 1, value + numbers[idx], target)
    bt(numbers, idx + 1, value - numbers[idx], target)

def solution(numbers, target):
    global answer 
    answer = 0
    bt(numbers, 0, 0, target)
    return answer

