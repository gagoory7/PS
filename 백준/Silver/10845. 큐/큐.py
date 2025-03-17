import math
import sys

input = sys.stdin.readline


n = int(input())

q = []

for _ in range(n) :
    s = input().split()

    if s[0] == 'push' :
        q.append(s[1])
    elif s[0] == 'pop' :
        if q :
            a = q.pop(0)
            print(a)
        else :
            print(-1)
    elif s[0] == 'size' :
        print(len(q))
    elif s[0] == 'empty' :
        if q :
            print(0)
        else :
            print(1)
    elif s[0] == 'front' :
        if q :
            print(q[0])
        else :
            print(-1)
    elif s[0] == 'back' :
        if q :
            print(q[-1])
        else :
            print(-1)
