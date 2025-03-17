import sys

input = sys.stdin.readline

n, p, q = map(int,input().split())

dp = {0: 1 }

def A(i) :
    global dp
    al = dp.get(i,None)
    if al :
        return al
    ap = A(i // p)
    aq = A(i // q)
    dp[i] = ap + aq
    return ap + aq

print(A(n))