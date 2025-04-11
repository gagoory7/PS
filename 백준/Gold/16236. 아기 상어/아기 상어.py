import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n)]


dx = [-1,0,0,1]
dy = [0,-1,1,0]

size = 2
eat_count = 0

def bfs(x, y):
    global size, eat_count
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    q = deque()
    q.append((x, y, 0))
    fish_list = []

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graphs[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < graphs[nx][ny] < size:
                        fish_list.append((dist + 1, nx, ny))
                    q.append((nx, ny, dist + 1))

    if not fish_list:
        return -1, -1, -1

    fish_list.sort()
    dist, nx, ny = fish_list[0]
    eat_count += 1
    if eat_count == size:
        size += 1
        eat_count = 0
    graphs[nx][ny] = 0
    return nx, ny, dist

s_i, s_j = 0,0
for i in range(n) :
    for j in range(n) :
        if graphs[i][j] == 9 :
            s_i, s_j = i, j
            graphs[i][j]= 0 


time = 0

while True :
    x,y,count = bfs(s_i,s_j)
    if count == -1 :
        break
    else :
        time += count
        s_i, s_j = x,y



print(time)