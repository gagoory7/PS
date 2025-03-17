import heapq
n = int(input())

meetings = sorted([list(map(int,input().split())) for _ in range(n)])

rooms = []

for s,e in meetings :
    if rooms and rooms[0] <= s :
        heapq.heappop(rooms)
        
    heapq.heappush(rooms,e)

print(len(rooms))