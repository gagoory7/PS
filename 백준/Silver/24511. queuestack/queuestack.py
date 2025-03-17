# 24511
import sys
from collections import deque

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

insert_list = list(map(int,sys.stdin.readline().split()))

questack = deque()

for i in range(n):
    if a[i] == 0 :
        questack.appendleft(b[i])

for x in insert_list :
    questack.append(x)
    x = questack.popleft()
    print(x, end = ' ')