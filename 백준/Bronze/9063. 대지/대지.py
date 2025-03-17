import sys

input = sys.stdin.readline


x, y = [],[]
for i in range(int(input())):
    m,n = map(int,input().split())
    x.append(m)
    y.append(n)


print( ((max(x)-min(x))* (max(y)-min(y))))