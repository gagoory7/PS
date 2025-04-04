import heapq
import sys

input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
dist = [float('inf')] * (v+1)
heap = []
graphs = [ [] for _ in range(v+1)]

for _ in range(e) :
    a,b,w = map(int,input().split())
    graphs[a].append((w,b))
    
def Dijstra(start) :
    dist[start] = 0
    heapq.heappush(heap,(0,start))
    while heap :
        d, x = heapq.heappop(heap)
        if dist[x] < d:
            continue
        
        for w, next in graphs[x] :
            next_d = w + d
            if dist[next] > next_d :
                dist[next] = next_d
                heapq.heappush(heap,(next_d,next))

Dijstra(k)
for i in range(1,v+1) :
    print("INF" if dist[i] == float('inf') else dist[i])