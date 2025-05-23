from collections import deque
import sys

input = sys.stdin.readline

n , l =map(int,input().split())
nums = list(map(int,input().split()))

q = deque()

for i in range(n) :
    while q and q[-1][1] >= nums[i] :
        q.pop()
    q.append((i,nums[i]))
    if q[0][0] <= i-l :
        q.popleft()
    print(q[0][1],end=' ')