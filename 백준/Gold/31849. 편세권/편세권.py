import sys
input = sys.stdin.readline

from collections import deque

n, m, r, c = map(int,input().split())

houses = [ list(map(int,input().split())) for _ in range(r)]
factories = [ tuple(map(int,input().split())) for _ in range(c)]

distance = [[-1]*m for _ in range(n)]

def bfs():
    q = deque()
    for x, y in factories:
        x -= 1
        y -= 1
        q.append((x, y))
        distance[x][y] = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

bfs()

answer = float('inf')
for a, b, p in houses:
    a -= 1
    b -= 1
    if distance[a][b] != -1:
        answer = min(answer, distance[a][b] * p)

print(answer)