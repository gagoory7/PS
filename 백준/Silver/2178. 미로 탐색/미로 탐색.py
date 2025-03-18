from collections import deque
n, m = map(int,input().split())

graphs = [ list(map(int,input())) for _ in range(n) ] 
dx = [1,-1,0,0]
dy = [0,0,1,-1]



def bfs(x,y) :

    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >=m :
                continue
    
            if graphs[nx][ny] == 0 :
                continue

            if graphs[nx][ny] == 1 :
                graphs[nx][ny] = graphs[x][y] +1
                q.append((nx,ny))
    return graphs[n-1][m-1]
    
print(bfs(0,0))
