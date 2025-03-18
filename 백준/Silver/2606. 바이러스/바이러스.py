from collections import deque

t = int(input())
n = int(input())


graphs = [ []*(t+1) for _ in range(t+1)]

for _ in range(n) :
    a,b = map(int,input().split())
    graphs[a].append(b)
    graphs[b].append(a)

virus = 1

visited = [0]*(t+1)
count = 0

def bfs(x) :
    global count
    visited[x] = 1
    q = deque()

    q.append(x)

    while q :
        target = q.popleft()

        for i in graphs[target] :
            if visited[i] == 0 :
                visited[i] = 1
                q.append(i)
                count += 1
    print(count)
    

bfs(virus)