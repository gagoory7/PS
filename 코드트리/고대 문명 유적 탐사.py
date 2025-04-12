from collections import deque
import sys

sys.setrecursionlimit(1000000)


# # with open('input.txt', 'r') as f:
# #      lines = f.read().splitlines()
# # k, m = map(int, lines[0].split())
# # graphs = [list(map(int, line.split())) for line in lines[1:6]]
# nums = list(map(int, ' '.join(lines[6:]).split()))

k,m = map(int,input().split())
graphs = [list(map(int,input().split())) for _ in range(5)]
nums = list(map(int,input().split()))


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def cal():
    score = 0 
    visited = [[False]*5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                check_list = bfs(i, j, graphs[i][j], visited)
                if len(check_list) >= 3:
                    score += len(check_list)
                    for x, y in check_list:
                        graphs[x][y] = 0 
    return score

def rotate_3(x, y, k): 
    for _ in range(k + 1):  
        tmp = [[0] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                tmp[j][2 - i] = graphs[x - 1 + i][y - 1 + j]

        for i in range(3):
            for j in range(3):
                graphs[x - 1 + i][y - 1 + j] = tmp[i][j]


def bfs(x,y,k,visited) :
    if k == 0 :
        return []
    q = deque()
    q.append((x,y))
    answer = []
    answer.append((x,y))
    visited[x][y] = True

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<5 and 0<=ny<5 :
                if not visited[nx][ny] and graphs[nx][ny] == k :
                    q.append((nx,ny)) 
                    visited[nx][ny] = True
                    answer.append((nx,ny))
    

    return answer 


def fill(idx):
    global graphs, nums, m
    for i in range(5):  # 세로 방향 (열 기준)
        for j in range(4, -1, -1):  # 아래에서 위로 (행 기준)
            if idx >= m:
                return idx
            if graphs[j][i] == 0:
                graphs[j][i] = nums[idx]
                idx += 1

    return idx


answer = []
def back(depth,max_score,idx) :
    global graphs
    if depth >= k :
        return
    
    saved_graphs = [row[:] for row in graphs]
    scores = []
    for i in range(1,4) : 
        for j in range(1,4) :
            for q in range(3) :
                graphs = [row[:] for row in saved_graphs]
                rotate_3(i,j,q)
                s = cal()
                if s >= 3 :
                    scores.append((s,q,i,j))
            

    if len(scores) == 0 :
        return
    graphs = [row[:] for row in saved_graphs]
    scores.sort(key=lambda x: (-x[0], x[1], x[3],x[2]))
    rotate_3(scores[0][2],scores[0][3],scores[0][1])
    score = 0
    idxx = idx

    while True :
        s = cal()
        score +=s
        if s == 0 :
            break
        else :
            idxx = fill(idxx)
       
        
    if score != 0 :
        answer.append(score)
    back(depth+1, 0, idxx)


back(0,0,0)

print(*answer, sep=' ')


# 10 43
# 5 7 3 1 4
# 1 6 2 2 3
# 5 2 6 7 5
# 7 1 2 3 2
# 2 2 1 7 7
# 6 7 4 3 3 1 6 6 6 6 3 5 1 5 2 5 1 7 5 6 6 7 6 5 2 2 4 1 5 1 3 7 2 7 2 5 6 3 7 7 2 7 1
