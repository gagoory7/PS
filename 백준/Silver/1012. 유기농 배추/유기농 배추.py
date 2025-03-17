from collections import deque

test = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(graph,x,y) :
    q = deque()
    q.append([x,y])
    graph[x][y] = 0

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 :
                q.append([nx,ny])
                graph[nx][ny] = 0


for _ in range(test):
    n,m, k = map(int,input().split())
    map_list = [[0] * m for _ in range(n)]
    for __ in range(k) :
        x,y = map(int,input().split())
        map_list[x][y] = 1 
    count = 0
    for i in range(n) :
        for j in range(m) :
            if map_list[i][j] == 1 :
                dfs(map_list,i,j)
                count +=1
    print(count)