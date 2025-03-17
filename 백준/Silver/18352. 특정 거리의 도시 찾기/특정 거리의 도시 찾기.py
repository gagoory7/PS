
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


cities = []
q = deque([(x, 0)])
visited[x] = True

while q:
    x, dist = q.popleft()

    if dist == k:
        cities.append(x)
        continue
    
    for i in graph[x]:
        if not visited[i]: # 결국 x로 부터 어떤 노드를 방문하기 위한 최소 거리(값, 가중치)는 탐색을 통해 먼저 방문된 경우에 정해질 것. 따라서 이후에는 방문할 필요가 없음. 그래서 방문하지 않은 노드에 대해서만 큐에 삽입.
            visited[i] = True 
            q.append((i, dist+1))

answer = sorted(cities)

print(*answer, sep="\n") if answer else print(-1)