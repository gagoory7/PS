import sys

input = sys.stdin.readline

n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n)]


def dfs(start, visited):
    for i in range(n):
        if start == i :
            continue

        if not visited[i] and graphs[start][i]:
            visited[i] = True
            dfs(i, visited)



for i in range(n) :
    visited = [False] * n
    dfs(i,visited)
    for j in range(n) :
        if visited[j] :
            graphs[i][j] = 1
    
for graph in graphs :
    print(*graph)