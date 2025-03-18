import sys

def dfs(x) :
    visited[x] = 1
    next = nums[x]
    if visited[next] == 0 :
        dfs(next)
    return
    
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 0
    n = int(input())
    nums = list(map(int,input().split()))
    
    visited = [0] * (n+1)
    nums.insert(0,0)
    for i in range(1,n+1) :
        if visited[i] == 0 :
            dfs(i)
            cnt +=1
    print(cnt)