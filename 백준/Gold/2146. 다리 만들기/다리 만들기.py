import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n) ]

num = 2

dx = [1,-1,0,0]
dy = [0,0,1,-1]

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

def bfs2(v):
  queue = deque()
  dist = [[-1]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if graphs[i][j]==v:
        dist[i][j] = 0
        queue.append([i,j])

  while queue:
    x, y = queue.popleft()
    for (w, h) in [[1,0],[0,1],[-1,0],[0,-1]]:
      dx, dy = x+w, y+h
      if 0<=dx<n and 0<=dy<n:
        if graphs[dx][dy] and graphs[dx][dy]!=v:
          return dist[x][y]
        elif (not graphs[dx][dy]) and dist[dx][dy]==-1:
          dist[dx][dy] = dist[x][y]+1
          queue.append([dx,dy])

  return int(1e9)
                
for v in range(2,num):
  answer = min(answer, bfs2(v))
print(answer)