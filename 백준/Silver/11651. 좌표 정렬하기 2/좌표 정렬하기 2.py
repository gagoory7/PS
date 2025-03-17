n = int(input())
coords = []

for i in range(n):
    n,m  = map(int,input().split())
    coords.append( [n,m])

coords.sort(key = lambda x : (x[1],x[0]))

for _ in coords:
    print(_[0],_[1])