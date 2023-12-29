from itertools import permutations
def solution(numbers):
    num = [i for i in numbers]                                 
#1) 주어진 숫자를 하나하나 떼어버리기/문자열로 들어가있음
    pnum = []
    for j in range(1,len(numbers)+1):
        pnum += list(permutations(num,j))                      
#2) 조합할 수 있는 숫자들을 만듬
    fpnum = [int(''.join(pnum[l])) for l in range(len(pnum))]  
#3) 문자열에서 숫자로 만들기
    sosu = []
    for l in fpnum:                                            
#4) 0과 1은 소수가 아니고, 2는 range 범위가 애매해서 따로 뺌,
                                                               
#그이후는 2~(n-1) 나눠서 하나라도 나눠떨어지면 소수가 아님
        if(l in [0,1]):  
            pass
        elif(l==2):      
            sosu.append(2)
        else:
            sosu.append(l)                                     
#일단 먼저 넣어놓고 아니면 다시 빼는 방식
            for k in range(2,l):
                if(l%k==0):
                    sosu.remove(l)
                    break
    return len(set(sosu))                                      
#5) 중복값은 제거하여 소수의 종류 개수를 출력함

            
    


