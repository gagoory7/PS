import sys
from collections import deque

N = int(sys.stdin.readline())
DQ = deque()
for _ in range(N):
    S = sys.stdin.readline().split()

    if S[0] == 'push':  
        DQ.append(int(S[1]))

    if S[0] == 'pop':   
        if DQ:   
            print(DQ.popleft())
        else:
            print(-1)

    if S[0] == 'size':  
        print(len(DQ))

    if S[0] == 'empty':
        if DQ:
            print('0')
        else:
            print('1')

    if S[0] == 'front':
        if DQ:
            print(DQ[0])
        else:
            print(-1)

    if S[0] == 'back':
        if DQ:
            print(DQ[-1])
        else:
            print(-1)
