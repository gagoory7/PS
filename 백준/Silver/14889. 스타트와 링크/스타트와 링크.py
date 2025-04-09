n = int(input())

graphs = [ list(map(int,input().split())) for _ in range(n) ]


visited = [False] * n
answer = 1e8

def backtracking(depth,x) :
    global answer 
    if depth == n//2 :
        temp1 = []
        temp2 = []

        for i in range(n) :
            if visited[i] :
                temp1.append(i)
            else :
                temp2.append(i)

        s = 0

        for i in range(n//2) :
            for j in range(n//2) :
                s -= graphs[temp1[i]][temp1[j]]
                s += graphs[temp2[i]][temp2[j]]

        answer = min(answer,abs(s))
        return
    for i in range(x,n) :
        if not visited[i] :
            visited[i] = True
            backtracking(depth+1,i+1)
            visited[i] = False

backtracking(0,0)

print(answer)