from collections import deque

def solution(maps):
    
    # 방향 설정
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    # 행/열 
    n, m = len(maps), len(maps[0])
    
    # queue 변수에 시작점인 (0,0) 넣기
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()  # queue에서 하나의 원소를 빼서 x, y에 대입
        
        for i in range(4):
            nx = x + dx[i]      # nx update 
            ny = y + dy[i]      # ny update
            
            # 조건 지정
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if maps[nx][ny] == 0 or maps[nx][ny] > 1:
                continue
            
            if nx == 0 and ny == 0:
                continue
            
            queue.append((nx, ny))
            maps[nx][ny] += maps[x][y]
            
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
        
    
    
    