from collections import deque

graphs = [ [list(map(int,input().split())) for _ in range(5) ] for _ in range(5)]

results = []
def permutation(n,arr, x) :
    if len(arr) == x :
        results.append(arr)
        return 
    
    for i in range(0,n) :
        if i not in arr :
            permutation(n,arr+[i],x)

permutation(5,[],5)

b = [[[0] * 5 for _ in range(5)] for _ in range(5)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]


result = 1e9


def rotate(b) :
    tmp = [[0]*5 for _ in range(5) ]
    for i in range(len(b)) :
        for j in range(len(b[0])) :
            tmp[i][j] = b[4-j][i]

    return tmp


def bfs(b) :
    global result
    q = deque()
    dist = [[[0,0,0,0,0] for _ in range(5) ] for _ in range(5) ]
    q.append((0,0,0))

    while q :
        x,y,h = q.popleft()
        if (x,y,h) == (4,4,4) :
            result = min(result,dist[4][4][4])
            if result == 12 :
                print(result)
                exit()
                
            return
        
        for i in range(6) :
            nx, ny, nh = x + dx[i], y + dy[i], h + dh[i]

            if nx<0 or nx>= 5 or ny < 0 or ny >=5 or nh < 0 or nh >=5 :
                continue
            elif b[nx][ny][nh] == 0 or dist[nx][ny][nh] != 0 :
                continue

            q.append((nx,ny,nh))
            dist[nx][ny][nh] = dist[x][y][h] + 1

def dfs(d) :
    global b
    if d == 5 :
        if b[4][4][4] :
            bfs(b)
        return
    
    for i in range(4) :
        if b[0][0][0] :
            dfs(d+1)
        b[d] = rotate(b[d])



def solve() :
    for d in results :
        for i in range(5) :
            b[d[i]] = graphs[i]
        dfs(0)

solve()

if result ==  1e9 :
    print(-1)
else :
    print(result)