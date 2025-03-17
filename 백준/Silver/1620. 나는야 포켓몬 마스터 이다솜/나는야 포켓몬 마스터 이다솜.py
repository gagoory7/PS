# 1620
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

dict1 = {}


for i in range(1,n+1):
    _ = input().strip()
    dict1[i] = _
    dict1[_] = i

for _ in range(m):
    a = input().strip()

    if a.isdigit():

        print(dict1[int(a)],end=' ')
        
    else:
        print(dict1[a],end=' ')