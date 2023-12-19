def solution(n, lost, reserve):
    #1) 일단 도난/여벌 반영된 리스트 생성
    cyb = [2 if(i in reserve) else 1 for i in range(1,n+1)]
    cyb = [cyb[j]-1 if(j+1 in lost) else cyb[j] for j in range(n)]
    #2) 값이 0인 애들에 대해 탐색
    idx = []
    for k in range(len(cyb)):
        if(cyb[k]==0):
            idx.append(k)
    for nowidx in idx:  #0인애들 주위만 알아보기
    #뭔가 조건문에 문제잇나바
        if((nowidx==0)&(cyb[nowidx+1]==2)):
            #뒤에만 알아보면 됨
            cyb[nowidx] = 1
            cyb[nowidx+1] -= 1
        elif((nowidx==(n-1))&(cyb[nowidx-1]==2)):  #맨 끝쪽 인덱스
            cyb[nowidx] = 1
            cyb[nowidx-1] -= 1
        else:
#########여기까지 풀다가... 더 고민해보겠습니다!!