import heapq
import sys

input = sys.stdin.readline

n = int(input())

list = []

for _ in range(n) :
    x = -int(input())
    if x == 0 :
        if list :
            print(-heapq.heappop(list))
        else :
            print(0)
    else :
        heapq.heappush(list,x)