import sys

input = sys.stdin.readline

b = int(input())
bs = list(map(int,input().split()))
w = int(input())
ws = list(map(int,input().split()))

b_max = sum(bs)

dp = [ [0]*(b_max+1) for _ in range(b+1)]

def cal(idx,weight) :
    if idx > b :
        return
    if dp[idx][weight] == 1 :
        return
    dp[idx][weight] = 1

    if idx < b :
        cal(idx+1,weight + bs[idx])
        cal(idx+1,abs(weight-bs[idx]))
        cal(idx+1,weight)
    
cal(0,0)

for ww in ws :
    if ww > b_max :
        print('N')
    
    elif dp[b][ww] == 1 :
        print('Y')
    else :
        print('N')