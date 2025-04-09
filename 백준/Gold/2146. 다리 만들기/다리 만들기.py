
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())


graphs = [ list(map(int,input().split())) for _ in range(n)]

num = 2

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs1(x,y) :
    global num
    q = deque()
    q.append((x,y))
    graphs[x][y] = num

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<n :
                if graphs[nx][ny] == 1:
                    q.append((nx,ny))
                    graphs[nx][ny] = num
            
    num +=1

for i in range(n) :
    for j in range(n) :
        if graphs[i][j] == 1 :
            bfs1(i,j)

            
def bfs2(num) :
    q = deque()

    dist = [[-1] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if graphs[i][j] ==  num :
                dist[i][j] = 0
                q.append((i,j))

    while q :
        x, y = q.popleft() 
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny < n :

                if graphs[nx][ny] != num and graphs[nx][ny] != 0 :
                    return dist[x][y]
                if graphs[nx][ny] == 0 and dist[nx][ny] == -1 :
                    dist[nx][ny] = dist[x][y] +1
                    q.append((nx,ny))
   

answer = 1e9

for i in range(2,num) :
    answer = min(answer,bfs2(i))
    
print(answer)