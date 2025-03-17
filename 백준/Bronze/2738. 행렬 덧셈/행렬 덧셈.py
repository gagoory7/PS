a,b = [], []

m,n = map(int,input().split())

for i in range(m) :
    row = list(map(int,input().split()))
    a.append(row)
    
for i in range(m) :
    row = list(map(int,input().split()))
    b.append(row)

for row in range(m):
    for col in range(n):
        print(a[row][col]+b[row][col], end=' ')
    print()