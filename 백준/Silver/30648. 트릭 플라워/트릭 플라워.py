from collections import deque
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
r = int(input())

visited = [ [False] * (r) for _ in range(r)]

def run(a,b) :
    count = 0
    visited[a][b] = True

    q = deque()
    q.append((a,b))
    while q :
        x,y = q.popleft()
        if x+y + 2 < r :
            x += 1
            y += 1  
        else :
            x = x//2
            y = y//2
            

        if visited[x][y] :
            return count + 1 
        else :
            visited[x][y] = True
            q.append((x,y))
            count +=1
        


print(run(a,b))