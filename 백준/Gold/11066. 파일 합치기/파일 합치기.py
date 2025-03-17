import sys

input = sys.stdin.readline

t = int(input())

def solve():
    K = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * K for _ in range(K)]
    
    for i in range(K - 1):
        dp[i][i + 1] = arr[i] + arr[i + 1]
    

    for i in range(K - 2, -1, -1):
        for j in range(i + 2, K):
            dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)]) + sum(arr[i:j + 1])
    
    print(dp[0][K - 1])
    
for _ in range(t) :
    solve()