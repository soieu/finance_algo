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

#정답코드!
def solution(n, lost, reserve):
    cyb = [2 if(i+1 in reserve) else 1 for i in range(n)]
    cyb = [cyb[j]-1 if(j+1 in lost) else cyb[j] for j in range(n)]
    
    #(1) 맨앞이면~맨마지막-1 이면 뒤로, (2) 맨마지막이면 하나 앞으로 - 이때 0인 애들의 주위가 2인지 확인함
    zero = []
    for k in range(len(cyb)):
        if(cyb[k]==0):
            zero.append(k)
            #여기까지 체육복개수가 0인 애들 찾음
    for kk in zero:
        if(kk==0):     #바로 뒤에거만 확인
            if(cyb[kk+1]==2):
                cyb[kk] = 1
                cyb[kk+1] = 1
            else:
                pass
        elif((kk > 0) & (kk < n-1)):   #얘네들은 바로앞 먼저, 그다음뒤도 확인
            if(cyb[kk-1]==2):
                cyb[kk] = 1
                cyb[kk-1] = 1
            elif(cyb[kk+1]==2):
                cyb[kk] = 1
                cyb[kk+1] = 1
        else:   #kk가 마지막일때(n-1)
            if(cyb[kk-1]==2):
                cyb[kk] = 1
                cyb[kk-1] = 1
    return len(cyb)-cyb.count(0)