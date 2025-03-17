import sys

input = sys.stdin.readline

t = int(input())
n = int(input())

graphs = [ set(map(int,input().split())) for _ in range(n)]

virus = set({1})

for i in range(n) :
    for graph in graphs :
        if virus & graph :
            virus = virus | graph

print(len(virus) - 1)