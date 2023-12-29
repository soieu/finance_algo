import math

def primenumber(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def backtracking(size, idx, num, numbers, make_numbers):
    if idx == size:
        if num != "" and primenumber(int(num)):
            make_numbers.add(int(num))
    else:
        for i in range(len(numbers)):
            backtracking(size, idx+1, num+numbers[i], numbers[:i] + numbers[i+1:], make_numbers)
        
def solution(numbers):
    numbers = [str(n) for n in numbers]
    make_numbers = set()
    
    for size in range(1, len(numbers)+1):
        backtracking(size, 0, '', numbers, make_numbers)
    print(make_numbers)
        
    return len(make_numbers)


