from collections import deque

# 이동할  네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, maps):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵에서 벗어난 경우 무시 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if maps[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return maps[n-1][m-1]
    
def solution(maps):
    answer = 0
    global n, m
    
    n = len(maps)
    m = len(maps[0])
    
    # BFS 이용
    answer = BFS(0, 0, maps)
    
    # 상대 팀 진영에 도착할 수 없을 때 -1 return
    return -1 if answer <= 1 else answer