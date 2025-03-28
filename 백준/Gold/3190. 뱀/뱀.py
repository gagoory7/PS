import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

graphs = [ [0]* n for _ in range(n)]

for _ in range(k) :
    a,b = map(int,input().split())
    graphs[a-1][b-1] = 1

l = int(input())

directions = {}
for _ in range(l) :
    a,b = input().split()
    directions[int(a)]= b


dx = [0,1,0,-1]
dy = [1,0,-1,0]
dd = 0

x,y = 0,0

count = 0
i = 0
snake = []

while True :
    snake.append((x,y))
    
    i +=1
    x = x + dx[dd]
    y = y + dy[dd]

    if x<0 or x >= n or y<0 or y >=n or graphs[x][y] == 2:
        break
    
    if not graphs[x][y] :
        a, b = snake.pop(0)
        graphs[a][b] = 0
    
    graphs[x][y] = 2

    if i in directions :

        if directions[i] == 'D' :
            dd = (dd+1) % 4
        else :
            dd = (dd-1) % 4

print(i)
        