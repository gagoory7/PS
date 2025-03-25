import sys
import heapq 

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(1) :
    nums = list(map(int,input().split()))
    for num in nums : 
        heapq.heappush(heap,num)


for _ in range(n-1) :
    nums = list(map(int,input().split()))
    for num in nums : 
        if num > heap[0] :
            heapq.heappop(heap)
            heapq.heappush(heap,num)

print(heap[0])