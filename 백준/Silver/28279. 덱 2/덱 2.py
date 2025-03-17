import sys
from collections import deque

N = int(sys.stdin.readline())
num_list = deque()

for _ in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    i = s[0]
    if i == 1 :
        num_list.appendleft(s[1])
    elif i == 2 :
        num_list.append(s[1])
    elif i == 3 :
        if num_list :
            print(num_list.popleft())
        else :
            print(-1)
    elif i == 4 :
        if num_list :
            print(num_list.pop())
        else :
            print(-1)
    elif i == 5 :
        print(len(num_list))
    elif i == 6 :
        if num_list :
            print(0)
        else :
            print(1)
    elif i == 7 :
        if num_list :
            print(num_list[0])
        else :
            print(-1)
    elif i == 8 :
        if num_list :
            print(num_list[-1])
        else :
            print(-1)