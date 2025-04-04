import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth,total,plus,minus,multiply,divide) :
    global maximum, minimum
    if depth == n :
        maximum = max(maximum,total)
        minimum = min(minimum,total)
        return
    
    if plus :
        dfs(depth+1,total + nums[depth],plus-1,minus,multiply,divide)
    if minus :
        dfs(depth+1,total - nums[depth],plus,minus-1,multiply,divide)
    if multiply :
        dfs(depth+1,total * nums[depth] ,plus,minus,multiply-1,divide)
    if divide :
        dfs(depth+1,int(total / nums[depth]),plus,minus,multiply,divide-1)

dfs(1,nums[0],operator[0],operator[1],operator[2],operator[3])

print(int(maximum))
print(int(minimum))