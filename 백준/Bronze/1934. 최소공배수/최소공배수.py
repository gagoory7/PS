# 1934 

n = int(input())
c = 0
for _ in range(n):
    a,b = map(int,input().split())
    c = a *b
    while b > 0 :
        a,b = b, a%b
    c = c/ a
    print(int(c))