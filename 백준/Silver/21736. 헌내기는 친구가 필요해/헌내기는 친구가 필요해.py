n,m = map(int,input().split())

graphs = [ list(input()) for _ in range(n) ]

a,b = 0,0


for i in range(n) :
    for j in range(m) :
        if graphs[i][j] == 'I' :
            a,b = i,j


visited = [ [0] * (m) for _ in range(n) ]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    q = []
    q.append((x,y))
    visited[x][y] = 1
    count = 0

    while q :
        x,y = q.pop()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m : 
                continue
            if not visited[nx][ny] and graphs[nx][ny] != 'X' :
                q.append((nx,ny))
                visited[nx][ny] = 1
                if graphs[nx][ny] == 'P' :
                    count +=1

    if count == 0 :
        count = 'TT'

    return count 

print(bfs(a,b))