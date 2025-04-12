from collections import deque
import sys


input = sys.stdin.readline

n,m,f = map(int,input().split())

ground = [list(map(int,input().split())) for m in range(n)]

square = [ [list(map(int,input().split())) for _ in range(m)] for _ in range(5) ]

strange = []

for _ in range(f) :
    x,y,d,v = map(int,input().split())
    ground[x][y] = 1
    strange.append((x,y,d,v,0))

###### 여기 

# with open('input.txt', 'r') as file:
#     lines = file.readlines()

# # 첫 줄 처리
# n, m, f = map(int, lines[0].split())

# # ground 처리 (n줄)
# ground = [list(map(int, lines[i+1].split())) for i in range(n)]

# # square 처리 (5장, 각 m줄)
# square = []
# start_line = 1 + n  # square 시작 라인
# for h in range(5):
#     layer = []
#     for i in range(m):
#         layer.append(list(map(int, lines[start_line + h * m + i].split())))
#     square.append(layer)

# # strange 리스트 처리
# strange = []
# start_strange = start_line + 5 * m
# for i in range(f):
#     x, y, d, v = map(int, lines[start_strange + i].split())
#     ground[x][y] = 1
#     strange.append((x, y, d, v, 0))

######## 여기

tmp = [ [0]*m for _ in range(m)]

for i in range(m) :
    for j in range(m) :
        tmp[i][j] = square[3][i][m-1-j]

square[3] = tmp


dx = [0,0,1,-1]
dy = [1,-1,0,0]

s_s_x,s_s_y = 0,0
for i in range(m) :
    for j in range(m) :
        if square[4][i][j] == 2 :
            s_s_x,s_s_y = i,j

tmp = False
g_t_s_x,g_t_s_y = 0,0
for i in range(n) :
    for j in range(n) :
        if not tmp :
            if ground[i][j] == 3 :
                g_t_s_x, g_t_s_y = i,j
                tmp = True

g_t_e_x, g_t_e_y = 0,0
for i in range(g_t_s_x-1,g_t_s_x+ m+1) :
    for j in range(g_t_s_y-1,g_t_s_y+ m+1) :
        if ground[i][j] == 0 :
            g_t_e_x,g_t_e_y = i,j

s_e_h, s_e_x, s_e_y = 0,m-1,0

if g_t_e_y == g_t_s_y + m :
    s_e_h = 0
    s_e_y = g_t_s_y + m - 1 - g_t_e_x

if g_t_e_y == g_t_s_y - 1:
    s_e_h = 1
    s_e_y = g_t_e_x - g_t_s_x

if g_t_e_x == g_t_s_x - 1 :
    s_e_h = 3
    s_e_y = g_t_e_y - g_t_s_y

if g_t_e_x == g_t_s_x + m :
    s_e_h = 2
    s_e_y = g_t_e_y - g_t_s_y 

total_end_x,total_end_y = 0,0
for i in range(n) :
    for j in range(n) :
        if ground[i][j] == 4 :
            total_end_x, total_end_y = i,j

def check_index(h,x,y) :
    if h == 0 :
        if x >= m :
            return -1,-1,-1
        if x < 0 :
            return 4,m-1-y,m-1
        if y <0 :
            return 2,x,m-1
        if y >= m :
            return 3,x,m-1
    if h == 1 :
        if x >= m :
            return -1,-1,-1
        if x < 0 :
            return 4,0,y
        if y <0 :
            return 3,x,0
        if y >= m :
            return 2,x,0
        
    if h ==2 :
        if x >= m :
            return -1,-1,-1 
        if x < 0 :
            return 4,m-1,y
        if y < 0 :
            return 1,x,m-1
        if y >= m :
            return 0,x,0
        
    if h == 3 :
        if x >= m :
            return -1,-1,-1
        if x < 0 :
            return 4,0,y
        if y <0 :
            return 1,x,0
        if y >= m :
            return 0,x,m-1
    if h == 4 :
        if x < 0 :
            return 3,0,y 
        if x>= m :
            return 2,0,y
        if y < 0 :
            return 1,0,x
        if y >= m :
            return 0,0,m-1-x
    return h,x,y


def bfs(h,x,y) :
    visited = [ [[False] * m for _ in range(m)] for _ in range(5)]
    visited[h][x][y] = True
    q = deque()

    q.append((h,x,y,0))

    while q :
        h,x,y,c= q.popleft()
        for i in range(4) :
            xi, yi = x + dx[i], y + dy[i]

            nh,nx,ny = check_index(h,xi,yi)
            if (nh,nx,ny) == (-1,-1,-1) :
                continue
            if [nh,nx,ny] == [s_e_h, s_e_x, s_e_y] :
                return c + 1
            if visited[nh][nx][ny] :
                continue

            if square[nh][nx][ny] == 0 :
                visited[nh][nx][ny] = True
                q.append((nh,nx,ny,c+1))
    return -1
count = bfs(4,s_s_x,s_s_y)

count +=1

if count == -1 :
    print(-1)
    sys.exit()

for x,y,d,v,can in strange :
    for i in range(1, (count//v) + 1 ) :
        if 0 <= x + dx[d] * i < n and 0 <= y + dy[d] * i < n and ground[x + dx[d] * i][y + dy[d] * i] == 0:
            ground[x + dx[d] * i][y + dy[d] * i] = 1
        else:
            break

if ground[g_t_e_x][g_t_e_y] == 1 :
    print(-1)
    sys.exit()

q = deque()
q.append((g_t_e_x,g_t_e_y))

result_flag  =  False
visited = [[count]*n for _ in range(n)]
while q :
    x,y = q.popleft()
    
    z = visited[x][y]

    for r, c, d, v, can in strange :
        if can == 1 :
            continue

        if z % v == 0 and 0<=r+dx[d] * (z//v) < n and 0<= c + dy[d] * (z//v) < n :
            if ground[r+dx[d] * (z//v)][c + dy[d] * (z//v)] == 0 :
                ground[r+dx[d] * (z//v)][c + dy[d] * (z//v)] = 1
            else :
                can = 1
    
    if x == total_end_x and y == total_end_y :
        print(visited[x][y])
        result_flag  =  True
        break

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx < n and 0 <= ny < n :
            if ground[nx][ny] == 0 and visited[nx][ny] == count :
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] +1
            
            if ground[nx][ny] == 4 and visited[nx][ny] == count :
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] +1

if result_flag == False :
    print(-1)


# 20 8 6
# 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1 0 1 1 0 0
# 0 0 1 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0
# 0 1 0 0 0 1 1 0 1 0 1 0 0 0 1 0 0 0 0 1
# 0 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0
# 1 0 0 0 0 0 0 1 3 3 3 3 3 3 3 3 1 0 1 1
# 0 0 0 0 0 0 0 1 3 3 3 3 3 3 3 3 1 1 0 0
# 0 0 0 0 1 1 0 0 3 3 3 3 3 3 3 3 1 1 1 0
# 0 0 0 1 0 0 1 1 3 3 3 3 3 3 3 3 1 0 0 1
# 0 0 1 0 0 0 0 1 3 3 3 3 3 3 3 3 1 0 0 0
# 1 0 0 0 0 0 0 1 3 3 3 3 3 3 3 3 1 0 0 0
# 1 0 1 1 0 0 0 1 3 3 3 3 3 3 3 3 1 0 1 0
# 1 0 0 1 1 1 1 1 3 3 3 3 3 3 3 3 1 0 0 0
# 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 1 0 0 1 0 1 0 0 0 1 0 0 0 0 0 1 1 0 1
# 0 1 1 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0
# 0 1 0 1 1 0 0 1 0 1 4 1 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0
# 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1 1 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 0 0 0 0 0 1 1 1
# 1 0 0 1 1 1 1 1
# 1 0 0 1 1 1 1 1
# 1 0 0 1 1 1 1 1
# 1 1 0 1 1 1 1 1
# 1 1 0 1 1 1 1 1
# 1 0 0 1 1 1 1 1
# 1 1 0 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 0 0
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 2 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 13 14 2 25
# 0 2 1 3
# 9 18 0 8
# 10 17 2 4
# 2 9 1 10
# 18 2 0 11