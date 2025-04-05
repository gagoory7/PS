from collections import deque

L, N, K = map(int, input().split())
lamps = list(map(int, input().split()))

darkness = [1e9] * (L + 1)
visited = [False] * (L + 1)

queue = deque()

# 가로등에서 BFS 시작
for lamp in lamps:
    queue.append((lamp, 0))
    visited[lamp] = True
    darkness[lamp] = 0

while queue:
    x, dist = queue.popleft()

    for dx in [-1, 1]:
        nx = x + dx
        if 0 <= nx <= L and not visited[nx]:
            visited[nx] = True
            darkness[nx] = dist + 1
            queue.append((nx, dist + 1))

# 정렬하고 K개 출력
darkness.sort()
cnt = 0
for d in darkness:
    print(d)
    cnt += 1
    if cnt == K:
        break
