import sys
input = sys.stdin.readline

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
visited = [False] * n

def backtracking(depth, idx):
    global answer

    if depth == n // 2:
        team1 = []
        team2 = []
        
        for i in range(n):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        
        s1, s2 = 0, 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                s1 += graphs[team1[i]][team1[j]]
                s2 += graphs[team2[i]][team2[j]]
        
        answer = min(answer, abs(s1 - s2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth + 1, i + 1)
            visited[i] = False

backtracking(0, 0)
print(answer)