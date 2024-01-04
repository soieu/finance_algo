def solution(numbers, target):
    cnt = 0
    leaves = [0]
    for n in numbers:
        
        lst = []
        for l in leaves:
            lst.append(l+n)
            lst.append(l-n)
            
        leaves = lst
    
    return (leaves.count(target))
    