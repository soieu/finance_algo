#추억점수
#1) 처음엔 리스트 각각 비교해서 할까... - 너무 비효율적
#2) 딕셔너리를 생성해서 바로바로 그리움점수를 가져오자

name = ['may','kein','kain','radi']
yearning = [5,10,1,3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
new = dict()
answer = []
for i in range(len(name)):  #이름과 그리움 점수에 대한 딕셔너리 만들기
    new[name[i]] = yearning[i]
for p in photo:
    score = 0
    for j in range(len(p)):
        if(p[j] in new):
            score += new[p[j]]
    answer.append(score)
print(answer)