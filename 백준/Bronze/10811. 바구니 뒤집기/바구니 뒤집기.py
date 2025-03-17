m,n = map(int,input().split())

busket = list(range(m+1))
busket.pop(0)

for i in range(n):
  x,y = map(int,input().split())
  test = busket.copy()
  for j in range(y-x):
    busket[x+j-1] = test[y-j-1] 
    busket[y-j-1] = test[x+j-1]
 

[print(x) for x in busket]