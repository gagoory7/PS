import sys

input = sys.stdin.readline

n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n)]


def dfs(start) :
    for i in range(n) :
        if graphs[start][i] == 1 and visited[i] == 0 :
            visited[i] = 1
            dfs(i)



for i in range(n) :
    visited = [False] * n
    dfs(i)
    for j in range(n) :
        if visited[j] :
            graphs[i][j] = 1
    
for graph in graphs :
    print(*graph)
    