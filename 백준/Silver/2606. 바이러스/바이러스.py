import sys

input = sys.stdin.readline

t = int(input())        # 총 컴퓨터 수
n = int(input())        # 연결된 쌍의 수

# 그래프 초기화 (주의: []*(t+1)은 잘못된 방식)
graphs = [[] for _ in range(t+1)]

# 간선 정보 입력받기
for _ in range(n):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

visited = [0] * (t+1)
count = 0

# DFS 정의
def dfs(x):
    global count
    visited[x] = 1
    for i in graphs[x]:
        if not visited[i]:
            count += 1
            dfs(i)

# 1번 컴퓨터에서 시작
dfs(1)

# 결과 출력: 감염된 컴퓨터 수 (1번은 제외)
print(count)