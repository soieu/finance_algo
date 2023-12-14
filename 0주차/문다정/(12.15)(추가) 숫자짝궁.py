from collections import Counter
def solution(X, Y):
    #1) 일단 각자 받아온 숫자들이 각각 몇개로 이루어져있는지 살피기
    a = Counter(X); b = Counter(Y)
    #2) 숫자 종류가 적은애들을 긴애들에 잇는지만 확인! - 짜피 긴애들에 잇는데 적은애들에 없으면 성립 X
    if(len(a)>len(b)): #숫자종류 적은애들은 y로 설정
        x,y = a,b
    else:
        x,y = b,a
    #3) y에서 차례대로 살펴보기
    num = []  #최종적으로 숫자 넣을 리스트, 개수
    for ynum, ycnt in y.items():
        if(ynum in x):
            for j in range(min(x[ynum], ycnt)):
                num.append(int(ynum))
    if(len(num)==0):
        return '-1'
    #4) 그리고 안에 있는 거 정렬
    elif((num.count(0)==len(num))):
        return '0'      #0 밖에 없으면 걍 출력값은 0 (000 이런식 출력은 안됨)
    else:   
        num.sort(reverse=True)
        return ''.join([str(k) for k in num])


#기억할 부분
#1) collections 라이브러리 Counter : 리스트나 문자열에 대해서 원소별로 몇개씩 들었는지 반환(딕셔너리 형태로)
#2) "".join(리스트) : 리스트 내에 있는 원소들을 하나의 문자열로 결합
    