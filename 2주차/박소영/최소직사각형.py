def solution(sizes):
    answer = 0
    min_max = 0
    max_max = 0
    for card in sizes:
        min_max = max(min_max, min(card))
        max_max = max(max_max, max(card))
    
    answer = min_max * max_max
    return answer
