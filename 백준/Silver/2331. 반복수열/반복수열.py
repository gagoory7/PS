n,m = map(int,input().split())

dp = [0] * ((9**5)*5)
iteration = 1

def cal(a,b) :
    result = 0
    for i in str(a) :
        result += pow(int(i),b)
       
    return result

def dfs(n,m,iteration,dp) :
    if dp[n] != 0 :
        return dp[n] - 1
    
    dp[n] = iteration
    iteration += 1
    result = cal(n,m) 
    return dfs(result,m,iteration,dp)

print(dfs(n,m,iteration,dp))