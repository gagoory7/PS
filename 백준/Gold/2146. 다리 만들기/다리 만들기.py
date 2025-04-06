import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n) ]

num = 2

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 처음 섬 구분 
def bfs(x,y) :
    global num
    graphs[x][y] = num
    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n  and  0 <= ny < n :
                if graphs[nx][ny] == 1 :
                    q.append((nx,ny))
                    graphs[nx][ny] = num
    num+=1

for i in range(n) :
    for j in range(n) :
        if graphs[i][j] == 1 :
            bfs(i,j)


    
answer = 1e8

# 가장 가까운 섬 찾기 
def bfs2(v):
  q = deque()

  # 거리이자 좌표가 갔는지
  dist = [[-1]*n for _ in range(n)]

  # 섬 별 첫 시작 좌표
  for i in range(n):
    for j in range(n):
      if graphs[i][j]==v:
        dist[i][j] = 0
        q.append([i,j])

  while q:
    x, y = q.popleft()

    for i in range(4) :
       nx,ny = x + dx[i], y + dy[i]
       if 0<=nx<n and 0<=ny<n :
          if graphs[nx][ny] and graphs[nx][ny] != v:
             return dist[x][y]
          elif (not graphs[nx][ny]) and dist[nx][ny] == -1 :
             dist[nx][ny] = dist[x][y] +1
             q.append([nx,ny])

  return int(1e9)
                
# 섬 들 숫자로 넣기 

for v in range(2,num):
  answer = min(answer, bfs2(v))
print(answer)