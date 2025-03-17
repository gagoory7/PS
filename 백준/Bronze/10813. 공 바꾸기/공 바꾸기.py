m,n = map(int,input().split())

busket = list(range(m+1))
busket.pop(0)

for i in range(n):
  x,y = map(int,input().split())
  a = busket[x-1]
  busket[x-1] = busket[y-1]
  busket[y-1] = a

[print(x) for x in busket]