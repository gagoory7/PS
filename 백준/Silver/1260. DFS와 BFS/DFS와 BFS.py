import sys

input = sys.stdin.readline

def dfs(x):
    answer_dfs.append(x)
    dfsv[x] = 1

    for _n in graph[x] :
        if not dfsv[_n] :
            dfs(_n)

def bfs(x):
    q = []

    q.append(x)
    answer_bfs.append(x)
    bfsv[x] = 1

    while q :
        c = q.pop(0)
        for _n in graph[c] :
            if not bfsv[_n] :
                q.append(_n)
                answer_bfs.append(_n)
                bfsv[_n] = 1

n, m, v = map(int,input().split())

graph = [ [] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)) :
    graph[i].sort()

dfsv = [0] * (n+1)
bfsv = [0] * (n+1)
answer_dfs = []
answer_bfs = []

dfs(v)
bfs(v)
print(*answer_dfs)
print(*answer_bfs)