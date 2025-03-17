a = []
for _ in range(9):
    row = list(map(int,input().split()))
    a.append(row)
    
m = 0
x,y = 0,0
for row in range(9):
    for col in range(9):
        if m < a[row][col]:
            m = a[row][col]
            x=row
            y=col
            
print(m)
print(x+1, y+1)